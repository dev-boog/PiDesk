from flask import Flask, render_template

import socket
import requests

WINDOWS_PC_IP = "192.168.1.142"
WINDOWS_PORT = 42069

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/system')
def system():
    return render_template('system.html')

@app.route("/system/discord")
def open_discord():
    requests.post(
        f"http://{WINDOWS_PC_IP}:{WINDOWS_PORT}/command",
        json={"action": "discord"},
        timeout=2
    )
    return render_template('system.html')

if __name__ == '__main__':  
    app.run(host='0.0.0.0', port=1200, debug=True)
