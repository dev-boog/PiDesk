import socket
import threading

HOST = "0.0.0.0"
PORT = 5676

conn = None
connected = False
connection_status = "disconnected"  # "disconnected", "waiting", "connected", "failed"

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
    global conn, connected, connection_status

    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((HOST, PORT))
        server.listen(1)

        connection_status = "waiting"
        print(f"Waiting for PC connection on port {PORT}...")
        
        conn, addr = server.accept()
        print(f"Connected to {addr}")

        connected = True
        connection_status = "connected"

        threading.Thread(target=receive_messages, args=(conn,), daemon=True).start()

    except Exception as e:
        print(f"Connection failed: {e}")
        connection_status = "failed"


def start_connection():
    global connection_status

    if connected:
        print("Already connected")
        return

    if connection_status == "waiting":
        print("Already waiting for connection")
        return

    # Start connection listener in background thread
    threading.Thread(target=_connection_listener, daemon=True).start()


# Auto-start connection listener when module is imported
start_connection()
