from django.contrib import admin
from .views import *
from django.urls import path,include

urlpatterns = [
   path('',TreePlantation.as_view()),
   path('<int:pk>',TreeRetreive.as_view())
]