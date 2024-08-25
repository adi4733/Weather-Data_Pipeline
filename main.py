import json
from datetime import datetime, timezone
from functions import kelvin_to_fahrenheit
import pandas as pd
import requests

# # List of city names
#city_names = ['Portland']

with open('city_names.txt') as f:
    city_names = [line.strip() for line in f]

# Read the API key from a credential file
with open("credential.txt", "r") as f:
    api_key = f.read()

def get_weather_data(city_name):
    base_url = "https://api.openweathermap.org/data/2.5/weather?q="
    full_url = base_url + city_name + "&appid=" + api_key
    r = requests.get(full_url)
    data = r.json()
    return data

# Create an empty list to store DataFrames
all_weather_data = []

# Retrieve weather data for each city
for city in city_names:
    data = get_weather_data(city)
    df = pd.DataFrame([data])
    df=df.explode('weather')
    df[["long", "lat"]] = df["coord"].apply(pd.Series)
    df[["temp", "feels_like", "temp_min", "temp_max", "pressure", "humidity", "sea_level", "grnd_level"]] = df["main"].apply(pd.Series)
    df[["speed", "deg", "gust"]] = df["wind"].apply(pd.Series)
    df[["id",'main','description','icon']] = df["weather"].apply(pd.Series)
    df[["all"]] = df["clouds"].apply(pd.Series)
    df[["type", "id", "country", "sunrise", "sunset"]] = df["sys"].apply(pd.Series)
    df['sunrise_UTC'] = pd.to_datetime(df['sunrise'], unit='s')
    df['dt_utc'] = pd.to_datetime(df['dt'], unit='s')
    df['sunset_utc'] = pd.to_datetime(df['sunset'], unit='s')
    df.drop(columns=['coord', 'weather', 'main', 'wind', 'clouds', 'sys'], axis=1, inplace=True)
    all_weather_data.append(df)

# Combine all DataFrames into a single DataFrame
combined_weather_df = pd.concat(all_weather_data, ignore_index=True)


combined_weather_df = combined_weather_df.assign(
    temp_F=lambda x: kelvin_to_fahrenheit(x["temp"]),
    feels_like_F=lambda x: kelvin_to_fahrenheit(x["feels_like"]),
    temp_min_F=lambda x: kelvin_to_fahrenheit(x["temp_min"]),
    temp_max_F=lambda x: kelvin_to_fahrenheit(x["temp_max"])
)
combined_weather_df.rename(columns={
    "temp": "temp_k",
    "feels_like": "feels_like_k",
    "temp_min": "temp_min_k",
    "temp_max": "temp_max_k"
}, inplace=True)

# Print the combined DataFrame
print(combined_weather_df)





# city = data['name']
# weather_description = data['weather'][0]['description']
# temp_farhenheit = kelvin_to_fahrenheit(data['main']["temp"])
# feels_like_farhenheit = kelvin_to_fahrenheit(data['main']["feels_like"])
# min_temp_farhenheit = kelvin_to_fahrenheit(data['main']["temp_min"])
# max_temp_farhenheit = kelvin_to_fahrenheit(data['main']["temp_max"])
# pressure = data['main']['pressure']
# humidity = data['main']['humidity']
# wind_speed = data['wind']['speed']
# # time_of_record = datetime.utcfromtimestamp(data['dt']+data['timezone'])
# # sunrise_time = datetime.utcfromtimestamp(data['sys']['sunrise']+data['timezone'])
# # sunset_time = datetime.utcfromtimestamp(data['sys']['sunset']+data['timezone'])
# time_of_record = datetime.fromtimestamp(data['dt'] / 1000, tz=timezone.utc)
# sunrise_time = datetime.fromtimestamp(data['sys']['sunrise'] / 1000, tz=timezone.utc)
# sunset_time = datetime.fromtimestamp(data['sys']['sunset'] / 1000, tz=timezone.utc)
