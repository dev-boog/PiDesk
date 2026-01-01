from flask import Blueprint, render_template
from datetime import datetime

system_routes = Blueprint("system", __name__)

@system_routes.route('/system')
def system():
    return render_template('system.html')