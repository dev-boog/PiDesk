from flask import Blueprint, render_template
from datetime import datetime
from config.config_manager import get_application_shortcuts

system_routes = Blueprint("system", __name__)

# Fetch application shortcuts for system settings page
@system_routes.route('/fetch_application_shortcuts')
def fetch_application_shortcuts():
    shortcuts = get_application_shortcuts()
    shortcut_html = ""
    for key, app in shortcuts.items():
        display_name = app['display_name']
        file_path = app['file_path']
        shortcut_html += f'''
        <button onclick="', '{file_path}')" class="bg-violet-500/20 border border-violet-500/30 rounded-lg px-3 py-1.5 text-xs font-medium text-violet-200 cursor-pointer">
            {display_name}
        </button>
        '''
    return shortcut_html

@system_routes.route('/system')
def system():
    return render_template('system.html')