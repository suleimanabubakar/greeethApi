from django.contrib import admin
from .views import *
from django.urls import path,include

urlpatterns = [
    path('',OrganisationCreate.as_view()),
    path('addOfficial',AddOrganisationUser.as_view()),
    path('categories',Categories.as_view())
]