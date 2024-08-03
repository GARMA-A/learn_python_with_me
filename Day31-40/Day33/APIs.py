import requests

import requests
from datetime import datetime

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

# API PARAMS
# you can send params like that 
parameters = {
       "lat": 51.509865,
       "lng":-0.118092,
       "formatted":0
}
resWithParams = requests.get("https://api.sunrise-sunset.org/json" , params=parameters)
# or like that
resWithOutParams = requests.get("https://api.sunrise-sunset.org/json?lat=51.509865&lng=-0.118092")
resWithOutParams.raise_for_status()
print(resWithOutParams.status_code)
print(resWithOutParams.json())
# the parameteres is like 
# https://api.sunrise-sunset.org/json?lat=51.509865&lng=-0.118092


