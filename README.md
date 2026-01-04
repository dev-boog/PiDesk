# PiDesk

A Raspberry Pi-based desk companion that provides a touch-friendly web interface for displaying time, weather, and controlling your Windows PC remotely. Think of it as a DIY Stream Deck alternative with a dashboard.

## Hardware

- **Raspberry Pi 4** (4GB RAM recommended)
- **7-inch LCD Touchscreen** (800x480 official Raspberry Pi display or compatible)
- MicroSD card (16GB+)
- USB-C power supply (5V 3A)

## Features

- **Clock & Date Display** - Real-time clock with day and date
- **Weather Widget** - Current weather conditions using WeatherAPI
- **PC Remote Control** - Launch applications on your Windows PC from the Pi
- **Application Shortcuts** - Configurable shortcuts to launch apps on your main system
- **Touch-Optimized UI** - Designed for touchscreen displays with large tap targets
- **Particle Background** - Aesthetic particles.js animated background

## Architecture

The system consists of two parts:

1. **Pi Application** (this repo) - Runs on the Raspberry Pi, serves the web UI and listens for PC connections
2. **Windows Client** - Runs on your Windows PC, connects to the Pi and executes commands

```
┌─────────────────┐         Socket (5676)         ┌─────────────────┐
│  Raspberry Pi   │◄────────────────────────────►│   Windows PC    │
│  (Web Server)   │                               │   (Client)      │
│  Port 5420      │                               │                 │
└─────────────────┘                               └─────────────────┘
```

## Project Structure

```
PiDesk/
├── main.py                 # Entry point - starts Flask server & socket listener
├── requirements.txt        # Python dependencies
├── run.sh                  # Startup script for Pi (kiosk mode)
├── api_keys.json           # API keys (not in repo - see setup)
├── config/
│   ├── config_manager.py   # Configuration utilities
│   └── configs/
│       └── application_shortcuts.json  # PC app shortcuts config
├── connection/
│   └── concection.py       # Socket server for PC communication
└── web_application/
    ├── app.py              # Flask app initialization
    ├── routes/
    │   ├── home_route.py   # Home page & weather API
    │   ├── settings_route.py
    │   └── system_route.py # PC control & shortcuts
    ├── static/
    │   ├── clock.js        # Real-time clock updates
    │   ├── global.js       # Global utilities
    │   ├── navigation.js   # Widget toggle functionality
    │   ├── notification.js # Toast notifications
    │   └── particles-js_config.js
    └── templates/
        ├── home.html       # Main dashboard
        ├── settings.html   # Settings page
        ├── system.html     # PC control page
        └── pc_controls.html
```

## Setup

### Prerequisites

- Raspberry Pi (tested on Pi 4) with Raspberry Pi OS
- Python 3.9+
- Chromium browser (for kiosk mode)
- Windows PC on the same network

### Pi Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/PiDesk.git
   cd PiDesk
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create configuration files** (see [Configuration Files](#configuration-files) below)

5. **Run the application**
   ```bash
   python main.py
   ```

6. **Access the web interface**
   Open `http://<pi-ip-address>:5420` in a browser

### Kiosk Mode (Auto-start)

The `run.sh` script launches the app in kiosk mode:

```bash
chmod +x run.sh
./run.sh
```

To auto-start on boot, add to `/etc/xdg/lxsession/LXDE-pi/autostart`:
```
@/home/boog/Desktop/PiDesk/run.sh
```

## Configuration Files

These files are **not included in the repository** and must be created manually:

### `api_keys.json`

Contains API keys for external services. Create this file in the project root:

```json
{
    "weather_api_key": "YOUR_WEATHERAPI_KEY_HERE"
}
```

Get a free API key from [WeatherAPI.com](https://www.weatherapi.com/)

### `config/configs/application_shortcuts.json`

Defines application shortcuts that appear on the System page. These are apps on your **Windows PC** that can be launched remotely:

```json
{
    "discord": {
        "display_name": "Discord",
        "file_path": "C:/Users/YourUsername/AppData/Local/Discord/Update.exe"
    },
    "spotify": {
        "display_name": "Spotify",
        "file_path": "C:/Users/YourUsername/AppData/Roaming/Spotify/Spotify.exe"
    },
    "chrome": {
        "display_name": "Chrome",
        "file_path": "C:/Program Files/Google/Chrome/Application/chrome.exe"
    }
}
```

**Note:** Use forward slashes `/` in file paths, even for Windows paths.

## Windows Client

The Windows client connects to the Pi and listens for commands. Create these files on your Windows PC:

### `main.py` (Windows)

```python
import socket
import threading
import time

PI_IP_ADDRESS = "192.168.1.87"  # Change to your Pi's IP
PORT = 5676

def handle_command(command):
    if command.startswith("CMD:"):
        cmd = command[4:].strip()
        print(f"[Command received: {cmd}]")
        
        if cmd == "ping":
            print("Pong!")
        elif cmd == "status":
            print("Status: Running")
        else:
            print(f"Unknown command: {cmd}")
    else:
        print(f"Pi: {command}")

def receive_messages(sock):
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                print("Connection closed by Pi")
                break
            message = data.decode().strip()
            handle_command(message)
        except ConnectionResetError:
            print("Connection reset by Pi")
            break
        except Exception as e:
            print(f"Listener error: {e}")
            break

def connect_to_pi():
    while True:
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((PI_IP_ADDRESS, PORT))
            print("Connected to Raspberry Pi")
            return client
        except ConnectionRefusedError:
            print(f"Pi not ready. Retrying in 3 seconds...")
            time.sleep(3)
        except Exception as e:
            print(f"Connection error: {e}. Retrying in 3 seconds...")
            time.sleep(3)

client = connect_to_pi()
threading.Thread(target=receive_messages, args=(client,), daemon=True).start()

while True:
    msg = input("PC: ")
    client.sendall(msg.encode())
```

### `connect.py` (Windows - Optional utility class)

```python
import socket

class connect:
    PI_IP_ADDRESS = "192.168.1.87"  # Change to your Pi's IP
    PORT = 5676

    def listener(sock, command_handler=None):
        while True:
            try:
                data = sock.recv(1024)
                if not data:
                    print("Connection closed by Pi")
                    break
                
                message = data.decode().strip()
                print(f"Pi: {message}")
                
                if command_handler:
                    command_handler(message)
                    
            except ConnectionResetError:
                print("Connection reset by Pi")
                break
            except Exception as e:
                print(f"Listener error: {e}")
                break

    def connect():
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((connect.PI_IP_ADDRESS, connect.PORT))
        print("Connected to Raspberry Pi")
        return client
```

## Ports

| Port | Service | Description |
|------|---------|-------------|
| 5420 | HTTP | Flask web server |
| 5676 | TCP | Socket connection to Windows PC |

## Troubleshooting

### Connection Issues

1. **Pi not accepting connections**
   - Ensure both devices are on the same network
   - Check that port 5676 is not blocked by firewall
   - Verify the Pi's IP address: `hostname -I`

2. **Weather not loading**
   - Verify `api_keys.json` exists and contains a valid WeatherAPI key
   - Check the location query in `home_route.py` (default: "CT4")

3. **Touchscreen buttons hard to press**
   - The UI is optimized for touch with `touch-manipulation` CSS
   - Ensure you're using a supported browser (Chromium recommended)

## License

MIT License
