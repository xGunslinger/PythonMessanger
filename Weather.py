# Python program to find current
# weather details of any city
# using openweathermap api
# import required modules
import requests


api_key = 'dfbab7a810f3b135cc7b4366abfffc8e'
base_url = 'http://api.openweathermap.org/data/2.5/weather?'

def getWeather(city_name):
    complete_url = base_url + 'appid=' + api_key + '&q=' + city_name
    response = requests.get(complete_url)
    x = response.json()

    if x['cod'] != '404':
        y = x['main']
        current_temperature = y['temp']
        current_pressure = y['pressure']
        current_humidiy = y['humidity']
        z = x['weather']
        weather_description = z[0]['description']
        weather = ' Temperature = ' +\
                  str(current_temperature - 273.15) +\
                  '\n atmospheric pressure (in hPa unit) = ' +\
                  str(current_pressure) +\
                  '\n humidity (in percentage) = ' +\
                  str(current_humidiy) + '\n description = ' +\
                  str(weather_description)
        return str(weather)
    else:
        return str('City Not Found')