import requests

city_name = "Enter city name"
API_key = "da59bfd063198d7f563e678801ddaaec"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric"


response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print("Weather is ", data["weather"][0]["description"])
    print("Current Temperature is ", data["main"]["temp"])
    print("Current Temperature Feels like is ", data["main"]["feels_like"])
    print("Humidity is ", data["main"]["humidity"])