#!/bin/bash
VENV_PATH="/home/boog/Desktop/PiDesk/venv"
APP_PATH="/home/boog/Desktop/PiDesk"
URL="http://127.0.0.1:5420" 
source "$VENV_PATH/bin/activate"
cd "$APP_PATH"
python main.py &
sleep 3

DISPLAY=:0 chromium --kiosk --incognito --noerrdialogs --disable-infobars --disable-session-crashed-bubble "$URL"
