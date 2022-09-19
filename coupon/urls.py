from django.contrib import admin
from .views import *
from django.urls import path,include

urlpatterns = [
    path('create',CreateCoupon.as_view()),
    path('<str:code>',CouponDetails.as_view()),
    path('redeem/<str:code>',RedeemCouuponView.as_view()),
]
