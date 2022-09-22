from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(TreeMaintainance)
class MaintainanceAdmin(admin.ModelAdmin):
    list_display = ["tree","maintained_on","maintained_by","location","height","image"]