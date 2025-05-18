from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

API_KEY = "caa06fd32d2511265e135af540527a5f"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({'error': 'City is required'}), 400

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    try:
        data = response.json()
    except Exception as e:
        return jsonify({'error': 'Invalid JSON response from API'}), 500

    if response.status_code != 200:
        return jsonify({'error': data.get('message', 'Unknown error')}), response.status_code

    return jsonify({
        'city': data.get('name'),
        'country': data['sys'].get('country'),
        'temperature': data['main'].get('temp'),
        'feels_like': data['main'].get('feels_like'),
        'humidity': data['main'].get('humidity'),
        'pressure': data['main'].get('pressure'),
        'wind_speed': data['wind'].get('speed'),
        'description': data['weather'][0].get('description'),
        'icon': data['weather'][0].get('icon')
    })

if __name__ == '__main__':
    app.run(debug=True)
