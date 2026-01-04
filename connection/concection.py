import socket
import threading

HOST = "0.0.0.0"
PORT = 5676

conn = None
server_socket = None
connected = False
connection_status = "disconnected"
_listener_running = False  

def get_connection_status():
    return connection_status

def is_connected():
    return connected

def receive_messages(connection):
    global connected, connection_status
    while connected:
        try:
            data = connection.recv(1024)
            if not data:
                break
            print("PC:", data.decode())
        except:
            break

    print("Connection closed")
    connected = False
    connection_status = "disconnected"

def send_message(message):
    if not connected:
        print("Not connected")
        return False

    try:
        conn.sendall(message.encode())
        return True
    except Exception as e:
        print("Send failed:", e)
        return False


def _connection_listener():
    global conn, connected, connection_status, server_socket, _listener_running

    _listener_running = True
    
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((HOST, PORT))
        server_socket.listen(1)
        server_socket.settimeout(1.0)  

        connection_status = "waiting"
        print(f"Waiting for PC connection on port {PORT}...")
        
        while _listener_running:
            if not connected:
                connection_status = "waiting"
                try:
                    conn, addr = server_socket.accept()
                    print(f"Connected to {addr}")
                    connected = True
                    connection_status = "connected"
                    threading.Thread(target=receive_messages, args=(conn,), daemon=True).start()
                except socket.timeout:
                    continue  
                except OSError:
                    break  
            else:
                import time
                time.sleep(0.5)

    except Exception as e:
        print(f"Connection failed: {e}")
        connection_status = "failed"
    finally:
        _listener_running = False


def start_connection():
    global connection_status, _listener_running

    if connected:
        print("Already connected")
        return

    if _listener_running:
        print("Listener already running")
        return

    threading.Thread(target=_connection_listener, daemon=True).start()
