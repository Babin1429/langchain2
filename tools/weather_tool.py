from langchain.tools import tool
import requests
import os
from dotenv import load_dotenv

load_dotenv()

@tool
def weather(city: str) -> str:
    """Useful for getting the current weather of a city. Input should be a city name like 'Chennai' or 'London'."""
    try:
        api_key = os.getenv("WEATHER_API_KEY")
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        data = response.json()
        if data["cod"] == 200:
            temp = data["main"]["temp"]
            description = data["weather"][0]["description"]
            return f"Weather in {city}: {description}, Temperature: {temp}°C"
        else:
            return f"Could not get weather for {city}"
    except Exception as e:
        return f"Error getting weather: {str(e)}"
