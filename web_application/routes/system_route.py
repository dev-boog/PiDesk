from flask import Blueprint, render_template
from datetime import datetime
from config.config_manager import get_application_shortcuts

import connection.concection

system_routes = Blueprint("system", __name__)

@system_routes.route('/fetch_application_shortcuts')
def fetch_application_shortcuts():
    shortcuts = get_application_shortcuts()
    shortcut_html = ""
    for key, app in shortcuts.items():
        display_name = app['display_name']
        file_path = app['file_path'].replace('\\', '\\\\').replace("'", "\\'")
        shortcut_html += f'''
        <button onclick="launchApplication('{file_path}')" class="bg-violet-500/20 border border-violet-500/30 rounded-lg px-3 py-1.5 text-xs font-medium text-violet-200 cursor-pointer">
            {display_name}
        </button>
        '''
    return shortcut_html

@system_routes.route('/connection_status')
def connection_status():
    status = connection.concection.get_connection_status()
    
    if status != 'connected':
        return f'''
        <div id="connection-panel" hx-get="/connection_status" hx-trigger="every 2s" hx-swap="outerHTML">
            <div class="bg-[#1a1a2e]/80 backdrop-blur-md border border-white/10 rounded-xl p-5 text-white break-inside-avoid">
                <p class="text-[10px] text-white/40 uppercase tracking-wider mb-3">Connection Status</p>
                <p class="text-base font-medium text-white mb-2">Connection to your main system was not successful. Please make sure the PiDesk software is running on your main system and that both devices are on the same network.</p>
                <p class="text-xs text-white/40 mb-2">Status: {status}</p>
            </div>
        </div>
        '''
    else:
        return f'''
        <div id="connection-panel" hx-get="/connection_status" hx-trigger="every 5s" hx-swap="outerHTML">
            <div class="bg-[#1a1a2e]/80 backdrop-blur-md border border-white/10 rounded-xl p-5 text-white break-inside-avoid">
                <p class="text-[10px] text-white/40 uppercase tracking-wider mb-3">Application Shortcuts</p>
                <div class="flex gap-2 flex-wrap" hx-get="/fetch_application_shortcuts" hx-trigger="load" hx-swap="innerHTML">
                    <!-- Buttons loaded via HTMX -->
                </div>
            </div>
        </div>
        '''

@system_routes.route('/system')
def system():
    connection_status = connection.concection.get_connection_status()
    return render_template('system.html', connection_status=connection_status)