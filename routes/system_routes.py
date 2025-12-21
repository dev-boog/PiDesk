from flask import Blueprint, render_template
from config import APP_PATHS
from client import launch_program, send_command

system_routes = Blueprint("system", __name__)

# Display the system page
@system_routes.route('/system')
def system():
    """System page."""
    return render_template('system.html')

# Launch a specified application
@system_routes.route("/launch/<app_name>")
def launch_app(app_name):
    if app_name in APP_PATHS:
        launch_program(APP_PATHS[app_name])
    else:
        print(f"[ERROR] Unknown app: {app_name}")
    return render_template('system.html')

# Send a system command
@system_routes.route("/send_command/<command_name>")
def send_command_route(command_name):
    """Send system command (shutdown, restart, volume_mute)."""
    send_command(command_name)
    return render_template('system.html')
