from rest_framework.serializers import *
from .models import *


class CurrencyConvertSerailizer(ModelSerializer):
    class Meta:
        model = PointToCurrency
        fields = ['points']


class CurrencySerializer(ModelSerializer):
    point = CurrencyConvertSerailizer(read_only=True)
    class Meta:
        model = Currency
        fields = ['pk','name','point']
    

