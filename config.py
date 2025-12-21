import json

with open("./config.json", "r") as f:
    _config = json.load(f)

WINDOWS_PC_IP = _config.get("connection", {}).get("WINDOWS_PC_IP", "127.0.0.1")
WINDOWS_PORT = _config.get("connection", {}).get("WINDOWS_PC_PORT", 42069)
APP_PATHS = _config.get("application_shortcuts", {})
