from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Tree)
class TreeAdmin(admin.ModelAdmin):
    list_display = ["id","created_on","planter","location","height","image","age"]