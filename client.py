import requests
from config import WINDOWS_PC_IP, WINDOWS_PORT
import subprocess
import os
import platform

BASE_URL = f"http://{WINDOWS_PC_IP}:{WINDOWS_PORT}"

def launch_program(path):
    """
    Launch a program on Windows without crashing Flask.
    """
    try:
        if platform.system() != "Windows":
            subprocess.Popen([path])
            print(f"[INFO] Launched on non-Windows: {path}")
            return

        # Try os.startfile first
        try:
            os.startfile(path)
            print(f"[INFO] Launched: {path}")
            return
        except OSError as e:
            # Catch the common OSError when Flask thread can't detect GUI
            print(f"[WARNING] os.startfile failed but continuing: {e}")

        # Fallback to subprocess
        try:
            subprocess.Popen(path, shell=True)
            print(f"[INFO] Launched via subprocess: {path}")
        except Exception as e:
            print(f"[ERROR] subprocess failed to launch {path}: {e}")

    except Exception as e:
        print(f"[ERROR] Unexpected error launching {path}: {e}")


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
