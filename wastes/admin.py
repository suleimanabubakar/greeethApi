from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(WasteType)
class WasteTypeAdmin(admin.ModelAdmin):
    list_display = ["name",]


@admin.register(RecycleWaste)
class RecycleWasteAdmin(admin.ModelAdmin):
    list_display = ["waste_type","quantity","price","location","created_on","owner","status"]


@admin.register(WasteBid)
class WasteBidAdmin(admin.ModelAdmin):
    list_display = ["waste","price","created_on","owner","status"]


@admin.register(SoldWaste)
class SoldWasteAdmin(admin.ModelAdmin):
    list_display = ["waste","price","bid","transacted_on"]