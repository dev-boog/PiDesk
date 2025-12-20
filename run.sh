#!/bin/bash

VENV_PATH="/home/boog/Desktop/PiDesk/venv"
APP_PATH="/home/boog/Desktop/PiDesk"
URL="http://127.0.0.1:5000"

# Activate virtualenv
source "$VENV_PATH/bin/activate"

# Start Flask app
cd "$APP_PATH"
python main.py &

# Give Flask time to start
sleep 3

# Launch Chromium in kiosk mode (Pi-safe)
DISPLAY=:0 chromium-browser \
  --kiosk \
  --incognito \
  --noerrdialogs \
  --disable-infobars \
  --disable-session-crashed-bubble \
  --disable-gpu \
  --disable-software-rasterizer \
  --disable-dev-shm-usage \
  --no-first-run \
  --no-default-browser-check \
  "$URL"
