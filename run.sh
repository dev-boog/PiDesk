#!/bin/bash
VENV_PATH="/home/boog/Desktop/PiDesk/venv"
APP_PATH="/home/boog/Desktop/PiDesk"
URL="http://127.0.0.1:5420" 
PORT=5420

# Kill any existing process on the port
fuser -k $PORT/tcp 2>/dev/null

source "$VENV_PATH/bin/activate"
cd "$APP_PATH"
python main.py &
PYTHON_PID=$!
sleep 3

DISPLAY=:0 chromium --kiosk --incognito --noerrdialogs --disable-infobars --disable-session-crashed-bubble "$URL"

# When Chromium exits, kill the Python server
kill $PYTHON_PID 2>/dev/null
fuser -k $PORT/tcp 2>/dev/null
