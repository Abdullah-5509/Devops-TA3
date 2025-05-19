
# Weather App

A simple weather forecast application built with *Flask* that allows users to search for a city and get current weather data like temperature, humidity, wind speed, and pressure using the *OpenWeatherMap API*.

## Features

- Search weather by city name
- Displays:
  - Temperature
  - Weather Description
  - Humidity
  - Wind Speed
  - Pressure
- Beautiful and responsive UI
- Built with Flask and served as a web app
- Dockerized for easy deployment

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/weather-app.git
cd weather-app/api


---

2. Install Requirements (For Local Python)

pip install -r requirements.txt

3. Run Locally

Make sure to set your OpenWeatherMap API key inside app.py.

python app.py

Visit: http://localhost:5000


---

Docker Usage

1. Build Docker Image

docker build -t weather-app .

2. Run Container

docker run -d -p 5000:5000 weather-app

Visit: http://localhost:5000


---

Testing with Selenium

Use test_weather.py to test the UI:

python test_weather.py

Ensure:

Chrome is installed

ChromeDriver matches Chrome version



---

Tech Stack

Python 3

Flask

HTML/CSS

OpenWeatherMap API

Docker

Selenium (for testing)



---

Screenshots

![WhatsApp Image 2025-05-19 at 10 25 58_03b051f8](https://github.com/user-attachments/assets/8079d59b-f8b3-42ca-ba48-1b4e27cd148d)



---

License

MIT License. Feel free to use and modify.


---

Author

Your Name
GitHub

---

Let me know if you'd like a version that includes *Kubernetes, **CI/CD with Jenkins, or **deployment to cloud platforms*.
