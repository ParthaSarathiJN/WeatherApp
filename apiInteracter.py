# Don't forget to add your API key in the APIKEY variable.

import requests
from decimal import *

# Insert the API key in APIKEY.


def WeatherFunction(PinCode, CountryCode):
	APIKEY = 'YourAPIkey'


	r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?zip={PinCode},{CountryCode}&appid={APIKEY}')
	weatherValues = r.json()

	# Checks for 4xx and 5xx errors
	if str(r.status_code)[2] == '4' or str(r.status_code)[2] == '5':

		ErrorCode = weatherValues['cod']
		result = f'Incorrect Pin Code or Country Abbreviation!\nError Code: {ErrorCode}'

	else:

		weatherKey = weatherValues['main']
		crntTemperature = weatherKey['temp']
		#crntPressure = weatherKey['pressure']
		crntMinTemp = weatherKey['temp_min']
		crntMaxTemp = weatherKey['temp_max']
		crntHumidity = weatherKey['humidity']

		#crntVisibility = weatherValues['visibility']

		#weatherWind = weatherValues['wind']
		#crntWindSpeed = weatherWind['speed']

		#weatherClouds = weatherValues['clouds']
		#crntClouds = weatherClouds['all']

		weatherWeather = weatherValues['weather']
		crntMain = weatherWeather[0]['main']
		crntDescription = weatherWeather[0]['description']

		result = f'Temperature = {"{:.2f}".format(crntTemperature-273.15)}°C,  Weather = {crntMain}({crntDescription}),  Humidity = {crntHumidity}%,\nMin.Temp = {"{:.2f}".format(crntMinTemp-273.15)}°C,  Max.Temp = {"{:.2f}".format(crntMaxTemp-273.15)}°C'

	return result


# print(resultOfWeather)
