from crewai.tools import tool
import requests
import os

@tool("Get the weather forecast for a given location and date")
def get_weather_forecast(location: str, date: str) -> str:
    """Get the weather forecast for a given location and date"""
    api_key = os.getenv("OPENWEATHER_API_KEY")
    city = clean_location(location)
    response = requests.get(
        f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
    )
    data = response.json()
    for entry in data["list"]:
        if date in entry["dt_txt"]:
            desc = entry["weather"][0]["description"]
            temp = entry["main"]["temp"]
            print(f"Forecast: {desc}, {temp}°C")
            return f"Forecast: {desc}, {temp}°C"
    print(f"No Forecast found for {date} in {city}")
    return "No forecast data found for this date"


def clean_location(location: str) -> str:
    if ',' in location:
        city = location.split(',')[0].strip()
        return city
    return location