from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(UserFootPrint)
class UserFootPrintAdmin(admin.ModelAdmin):
    list_display = ["user","home_emmission","travel_emmission","food_emmission","secondary_emmission","calculated_on"]