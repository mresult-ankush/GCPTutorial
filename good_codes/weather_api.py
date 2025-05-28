import requests
from typing import Optional

API_KEY = "YOUR_API_KEY"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather_data(city: str, api_key: str = API_KEY) -> Optional[dict]:
    try:
        response = requests.get(BASE_URL, params={"q": city, "appid": api_key})
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve data: {e}")
        return None

def display_weather(data: dict) -> None:
    try:
        weather = data["weather"][0]["main"]
        temp_kelvin = data["main"]["temp"]
        temp_celsius = temp_kelvin - 273.15
        print(f"Weather: {weather}")
        print(f"Temperature: {temp_celsius:.2f} °C")
    except (KeyError, TypeError):
        print("Invalid data format received.")

def main():
    city = input("Enter city name: ").strip()
    if not city:
        print("City name cannot be empty.")
        return

    data = get_weather_data(city)
    if data:
        display_weather(data)

if __name__ == "__main__":
    main()
