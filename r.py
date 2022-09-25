import requests
from greeeth.utils import get_weather,split,convert_str_date

res = get_weather('40.714224,-73.961452')
if res.status_code == 200:
    weather_data = res.json()
    dates = weather_data['moonriseTimeLocal']

    humidity = split(weather_data['daypart'][0]['relativeHumidity'],2)
    narrative = split(weather_data['daypart'][0]['narrative'],2)
    uvIndex = split(weather_data['daypart'][0]['uvIndex'],2)
    temperature = split(weather_data['daypart'][0]['temperature'],2)
    windSpeed = split(weather_data['daypart'][0]['windSpeed'],2)
    uvDesc = split(weather_data['daypart'][0]['uvDescription'],2)
    weather = split(weather_data['daypart'][0]['wxPhraseLong'],2)



        


else:
    print(res.status_code)