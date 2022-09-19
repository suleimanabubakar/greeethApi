from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import *
from .serializers import *
# Create your views here.


class Currencies(ListAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer