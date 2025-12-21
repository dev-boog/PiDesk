import requests
from config import WINDOWS_PC_IP, WINDOWS_PORT

BASE_URL = f"http://{WINDOWS_PC_IP}:{WINDOWS_PORT}"

def launch_program(path):
    """
    Ask the Windows PC to launch a program.
    `path` can be a string or list from APP_PATHS
    """
    try:
        response = requests.post(
            f"{BASE_URL}/launch_program",
            json={"file_path": path},
            timeout=5
        )
        if response.status_code == 200:
            print(f"[INFO] Launched: {path}")
        else:
            print(f"[ERROR] Failed to launch: {response.text}")
    except Exception as e:
        print(f"[ERROR] Could not contact Windows PC: {e}")

def send_command(command_name):
    """
    Send system commands to the Windows PC.
    """
    try:
        response = requests.post(
            f"{BASE_URL}/send_command",
            json={"command": command_name},
            timeout=5
        )
        if response.status_code == 200:
            print(f"[INFO] Command sent: {command_name}")
        else:
            print(f"[ERROR] Failed to send command: {response.text}")
    except Exception as e:
        print(f"[ERROR] Could not contact Windows PC: {e}")
