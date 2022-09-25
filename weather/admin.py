from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(CheckWeather)
class CheckWeatherAdmin(admin.ModelAdmin):
    list_display = ["date","timing","temperature","humidity","windspeed","uvIndex","uvDescription","tree","narrative"]
