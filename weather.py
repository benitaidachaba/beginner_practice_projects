
import requests

api_key = --
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city = input("Enter city name: ")
# This code fetches weather information for a given city using the OpenWeatherMap API.

def kelvin_to_celsius(kelvin):
    """Convert Kelvin to Celsius."""
    return kelvin - 273.15
def kelvin_to_fahrenheit(kelvin):
    """Convert Kelvin to Fahrenheit."""
    return (kelvin - 273.15) * 9/5 + 32


url = f"{base_url}appid={api_key}&q={city}"
response = requests.get(url).json()

if response["cod"] == 200:
    main = response["main"]
    weather = response["weather"][0]
    temp_celsius = kelvin_to_celsius(main["temp"])
    temp_fahrenheit = kelvin_to_fahrenheit(main["temp"])
    print(f"Weather in {city}:")
    print(f"Temperature: {temp_celsius:.2f}°C")
    print(f"Temperature: {temp_fahrenheit:.2f}°F")
    print(f"Description: {weather['description']}")
else:
    print("City not found.")
