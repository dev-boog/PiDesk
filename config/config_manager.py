import json

def get_application_shortcuts():
    with open('config/configs/application_shortcuts.json') as f:
        shortcuts = json.load(f)
    return shortcuts