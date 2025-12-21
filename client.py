import requests
from config import WINDOWS_PC_IP, WINDOWS_PORT, APP_PATHS

BASE_URL = f"http://{WINDOWS_PC_IP}:{WINDOWS_PORT}"

def launch_program(app_name):
    if app_name not in APP_PATHS:
        print(f"[ERROR] Unknown app: {app_name}")
        return

    path = APP_PATHS[app_name]

    try:
        response = requests.post(
            f"{BASE_URL}/launch_program",
            json={"file_path": path},
            timeout=5
        )
        if response.status_code == 200:
            print(f"[INFO] Launch request sent for {app_name}")
        else:
            print(f"[ERROR] Failed to send launch request: {response.text}")
    except Exception as e:
        print(f"[ERROR] Could not contact Windows PC: {e}")


def send_command(command_name):
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
