import signal
import sys
import threading
from werkzeug.serving import make_server
from web_application.app import app
from connection.concection import start_connection

PORT = 5420
server = None
shutdown_event = threading.Event()

def shutdown_server(signum=None, frame=None):
    if not shutdown_event.is_set():
        shutdown_event.set()
        print("\nShutting down server...")
        if server:
            threading.Thread(target=server.shutdown, daemon=True).start()

def run_flask():
    global server
    server = make_server('0.0.0.0', PORT, app, threaded=True)
    print(f"Flask server started on http://localhost:{PORT}")
    server.serve_forever()

if __name__ == '__main__':
    signal.signal(signal.SIGTERM, shutdown_server)
    signal.signal(signal.SIGINT, shutdown_server)
    
    # Start the socket server for PC connection
    start_connection()
    
    try:
        run_flask()
    except KeyboardInterrupt:
        shutdown_server()
    
    print("Server stopped.")
