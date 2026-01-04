from flask import Blueprint, render_template
from datetime import datetime
import requests
import json

home_routes = Blueprint("home", __name__)

# Home route | For getting current time, see clock.js
@home_routes.route('/')
@home_routes.route('/home')
def home():
    return render_template('home.html')

# Update the wether settings every hour | hx-get="/update_weather"
@home_routes.route('/update_weather')
def update_weather():
    with open('api_keys.json') as f:
        keys = json.load(f)
    api_key = keys['weather_api_key']
    api = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q=CT4&aqi=no"

    try:
        response = requests.get(api)
        if response.status_code == 200:
            data = response.json()
            location = data['location']['name']
            temp_c = data['current']['temp_c']
            condition = data['current']['condition']['text']            
            return f'''
            <div id="weather-location" hx-swap-oob="innerHTML">
                <p class="text-sm text-zinc-400">Location</p>
                <p class="text-base font-medium text-white">{location}</p>
            </div>
            <div id="weather-temp" hx-swap-oob="innerHTML">
                <p class="text-sm text-zinc-400">Temperature</p>
                <p class="text-base font-medium text-white">{temp_c}°C</p>
            </div>
            <div id="weather-condition" hx-swap-oob="innerHTML">
                <p class="text-sm text-zinc-400">Condition</p>
                <p class="text-base font-medium text-white">{condition}</p>
            </div>
            '''
    except Exception as e:
        print(f"Weather API error: {e}")
    pass