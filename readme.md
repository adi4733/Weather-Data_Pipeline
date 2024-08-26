## Weather Data Retrieval and Processing Script


### Overview

This script retrieves weather data for a list of cities from the OpenWeatherMap API, processes the data, and stores it in a Pandas DataFrame.

### Input Files

city_names.txt: a text file containing a list of city names, one city per line.

credential.txt: a text file containing the OpenWeatherMap API key.

### Output

A combined Pandas DataFrame containing weather data for all cities, with the following columns:

city: city name
long: longitude
lat: latitude
temp_k: temperature in Kelvin
temp_F: temperature in Fahrenheit
feels_like_k: feels like temperature in Kelvin
feels_like_F: feels like temperature in Fahrenheit
temp_min_k: minimum temperature in Kelvin
temp_min_F: minimum temperature in Fahrenheit
temp_max_k: maximum temperature in Kelvin
temp_max_F: maximum temperature in Fahrenheit
pressure: atmospheric pressure
humidity: humidity
wind_speed: wind speed
dt_utc: date and time of record in UTC
sunrise_utc: sunrise time in UTC
sunset_utc: sunset time in UTC
id: weather condition ID
main: weather condition main description
description: weather condition description
icon: weather condition icon
all: cloud coverage
type: system type
country: country code
sunrise: sunrise time in seconds
sunset: sunset time in seconds

### Functions

get_weather_data(city_name): retrieves weather data for a given city from the OpenWeatherMap API.

kelvin_to_fahrenheit(kelvin): converts temperature from Kelvin to Fahrenheit.
Script Flow

Reads the list of city names from city_names.txt.
Reads the OpenWeatherMap API key from credential.txt.
Retrieves weather data for each city using the get_weather_data function.
Processes the data for each city, extracting relevant information and converting temperatures from Kelvin to Fahrenheit.
Combines the data for all cities into a single Pandas DataFrame.
Prints the combined DataFrame.


### Note

This script assumes that the OpenWeatherMap API key is stored in a file named credential.txt in the same directory as the script. You should replace this file with your own API key. Additionally, you should update the city_names.txt file with the list of cities you want to retrieve weather data for.