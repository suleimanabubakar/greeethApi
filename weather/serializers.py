from rest_framework.serializers import ModelSerializer
from .models import *

class CheckWeatherSerailizer(ModelSerializer):
    class Meta:
        model = CheckWeather
        fields = '__all__'