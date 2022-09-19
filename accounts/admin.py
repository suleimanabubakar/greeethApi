from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from .models import CustomUser,Profile


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ["email","first_name","last_name","is_superuser","role"]
    search_fields = ['email']

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user","country","city","linkedin"]