from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ["pk","created_on","user","currency","user","value","points","status","code"]


@admin.register(Redeem)
class RedeemAdmin(admin.ModelAdmin):
    list_display = ["redeemed_by","redeemed_on","coupon"]