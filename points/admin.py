from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ["pk","name"]

@admin.register(PointToCurrency)
class PointToCurrencyAdmin(admin.ModelAdmin):
    list_display = ["currency","points"]