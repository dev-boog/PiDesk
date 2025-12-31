import threading
from web_application.app import app

def run_flask():
    app.run(host='0.0.0.0', port=5420, debug=False, use_reloader=False)

if __name__ == '__main__':
    flask_thread = threading.Thread(target=run_flask, daemon=True)
    flask_thread.start()
    
    print("Flask server started on http://localhost:5420")
    
    try:
        while True:
            pass  
    except KeyboardInterrupt:
        print("\nShutting down...")
