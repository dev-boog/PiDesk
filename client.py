import subprocess
import os
import platform

def launch_program(path):
    try:
        if isinstance(path, list):
            command = f'explorer "{path[1]}"'  
            subprocess.Popen(command, shell=True)
        elif isinstance(path, str):
            if platform.system() == "Windows":
                try:
                    os.startfile(path)
                except OSError:
                    subprocess.Popen(path, shell=True)
            else:
                subprocess.Popen([path])
        print(f"[INFO] Launched: {path}")
    except Exception as e:
        print(f"[ERROR] Failed to launch {path}: {e}")



def send_command(command_name):
    """
    Sends system commands (shutdown, restart, volume_mute).
    You need to implement actual Windows commands here.
    """
    print(f"[INFO] Command sent: {command_name}")
