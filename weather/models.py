from trees.models import Tree
from django.db import models

# Create your models here.

class CheckWeather(models.Model):
    date = models.DateField()
    timing = models.CharField(max_length=30,choices=[('day','day'),('night','night')])
    temperature = models.IntegerField()
    humidity = models.IntegerField()
    windspeed = models.IntegerField()
    weather = models.CharField(max_length=30)
    uvIndex = models.IntegerField()
    uvDescription = models.CharField(max_length=30)
    narrative = models.TextField()
    tree = models.ForeignKey(Tree,related_name="weather_checks",on_delete=models.CASCADE)



