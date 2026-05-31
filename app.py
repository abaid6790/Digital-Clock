from flask import Flask, render_template, request, jsonify
from datetime import datetime
import pytz
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder

app = Flask(__name__)

geolocator = Nominatim(user_agent="world_clock_web")
tf = TimezoneFinder()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_timezone', methods=['POST'])
def get_tz():
    city = request.json.get('city')
    try:
        location = geolocator.geocode(city)
        if location:
            tz_name = tf.timezone_at(lng=location.longitude, lat=location.latitude)
            return jsonify({"status": "success", "timezone": tz_name})
    except:
        pass
    return jsonify({"status": "error", "message": "City not found"})

if __name__ == '__main__':
    app.run(debug=True)