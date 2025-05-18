from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_KEY = "caa06fd32d2511265e135af540527a5f"  # <--- Make sure it's a valid key

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
        print("Error response:", data)  # Print exact issue from API
        return jsonify({'error': data.get('message', 'Unknown error')}), response.status_code

    return jsonify({
        'city': data.get('name'),
        'temperature': data['main'].get('temp'),
        'description': data['weather'][0].get('description')
    })

if __name__ == '__main__':
    app.run(debug=True)
