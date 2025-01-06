from app import app
from flask import request, render_template
import requests


API_KEY = 'fd30b2741c828ad55b5ceadc36318c73'

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    if request.method == 'POST':
        city = request.form['city']
        weather_data = get_weather(city)
    return render_template('index.html', weather=weather_data)

def get_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    print(response.status_code)
    if response.status_code == 200:
        forecast = []
        data = response.json()
        for item in data['list']:
            forecast.append({
                'date': item['dt_txt'],
                'temperature': item['main']['temp'],
                'description': item['weather'][0]['description'],
                'icon': item['weather'][0]['icon']
            })
        return forecast
    else:
        return None