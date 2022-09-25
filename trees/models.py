from django.contrib.gis.db import models
from accounts.models import CustomUser as User
from pathlib import Path
from datetime import datetime,date

from greeeth.utils import convert_str_date, get_reverse_location, get_weather,split,timing
# Create your models here.


def image_location(instance,filename):
    return Path(f'plantations/{instance.planter.pk}')/filename

class Tree(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    planter = models.ForeignKey(User,related_name="trees_planted",on_delete=models.CASCADE)
    location = models.PointField(geography=True,)
    height = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to=image_location)
    tree_type = models.CharField(max_length=40,null=True)
    planted_at = models.CharField(null=True,max_length=90)


    @property
    def age(self):
        planted_on = self.created_on.date()
        now= date.today()
        return (now-planted_on).days

   

    

    @property
    def address(self):
        if self.planted_at:
            return self.planted_at
        get_loc = get_reverse_location(self.location)
        if get_loc.status_code==200:
            encoded = get_loc.json()
            city = encoded.get('results')[0]['formatted']
        elif get_loc.status == 400:
            city = 'N/A'
        
    
        self.planted_at=city
        self.save() 
        return self.planted_at


    @property
    def weather(self):
        today = date.today()
        t = timing()
        try:
            return self.weather_checks.get(date=today,timing=t)
        except Exception as e:
            if checks := createWeatherChecks(self):
                return self.weather_checks.get(date=today,timing=t)
            else:
                return "N/A"
            

    @property
    def to_be_maintained(self):
        if self.weather == "N/A":
            return False
        weather = self.weather
        humidity = weather.humidity
        temperature  = weather.temperature
        return 40 <= humidity >= 50 and 38 <= temperature >= 60





    def addWeatherChecker(self,de_date,timing,temp,humidity,speed,uvIndex,uvDesc,nar,we):
        return self.weather_checks.create(date=de_date,timing=timing,temperature=temp,humidity=humidity,windspeed=speed,uvIndex=uvIndex,uvDescription=uvDesc,narrative=nar,weather=we)




def createWeatherChecks(tree):
    res = get_weather(tree.location)
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
        dayornight = split(weather_data['daypart'][0]['dayOrNight'],2)

        for i,d in enumerate(dates):
            correct_date = convert_str_date(d)
            for index,uv in enumerate(uvIndex[i]):
                uv = uv or 0
                w = weather[i][index] or 'N/A'
                uvD = uvDesc[i][index] or 'N/A'
                temp = temperature[i][index] or 0
                nar = narrative[i][index] or 'N/A'
                h = humidity[i][index] or 0
                speed = windSpeed[i][index] or 0
                nights = dayornight[i][index]


                n = 'day' if nights in [None, "D"] else 'night'
                tree.addWeatherChecker(correct_date,n,temp,h,speed,uv,uvD,nar,w)



        return "Success"
    else:
        print(res.status_code)
        return None