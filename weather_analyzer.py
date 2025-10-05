import requests
import json

city="Kathmandu"
API_key="8dc880c4bb2b9e670aa3339d20e449f1"
url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}"

response=requests.get(url)
data=response.json()
parsed_data=json.loads(data)  #parsing json string into python dictonary

weather_main=parsed_data["weather"][0]["main"]
weather_description = parsed_data["weather"][0]["description"]
temp = parsed_data["main"]["temp"]
feels_like = parsed_data["main"]["feels_like"]
humidity = parsed_data["main"]["humidity"]
wind_speed = parsed_data["wind"]["speed"]
wind_deg = parsed_data["wind"]["deg"]
city = parsed_data["name"]
country = parsed_data["sys"]["country"]



