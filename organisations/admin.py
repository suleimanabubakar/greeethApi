from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name",]
@admin.register(Organisation)
class Admin(admin.ModelAdmin):
    list_display = ["name","address","created_on","created_by","type"]

@admin.register(OrganisationOfficial)
class OrganisationOfficialAdmin(admin.ModelAdmin):
    list_display = ["user","organisation","assigned_on"]