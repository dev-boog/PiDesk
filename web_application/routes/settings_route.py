from flask import Blueprint, render_template
from datetime import datetime

settings_routes = Blueprint("settings", __name__)

@settings_routes.route('/settings')
def settings():
    return render_template('settings.html')