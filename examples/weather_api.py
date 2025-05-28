import requests

city = input("Enter city: ")
url = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=YOUR_API_KEY"
response = requests.get(url)
data = response.json()
print("Weather:", data["weather"][0]["main"])
print("Temperature:", data["main"]["temp"] - 273.15)
