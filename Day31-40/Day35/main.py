import requests

API_KEY = "20b34a9d7ccb5cd85e154737b6782279"

parameters = \
{
       "lat":30.033333,
       "lon":31.233334,
       "appid":API_KEY ,
       "cnt":4
}


res = requests.get('https://api.openweathermap.org/data/2.5/weather' , params=parameters)


res.raise_for_status()

weather_data = res.json()
print(weather_data)
