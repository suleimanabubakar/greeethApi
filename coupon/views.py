from codecs import lookup
from django.shortcuts import render
from rest_framework.generics import CreateAPIView,ListCreateAPIView,RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from coupon.serializers import CouponCreateSerializer,RedeemSerializer
from django.shortcuts import get_object_or_404, render

# Create your views here.

class CreateCoupon(ListCreateAPIView):
    serializer_class = CouponCreateSerializer
    queryset = Coupon.objects.all()

    def perform_create(self,serializer):
        serializer.save(user=self.request.user) 

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user,status="active")



class CouponDetails(RetrieveAPIView):
    serializer_class =  CouponCreateSerializer
    queryset = Coupon.objects.all()
    lookup_field = 'code'

    def get_queryset(self):
        return super().get_queryset().filter(status="active")


class RedeemCouuponView(CreateAPIView):
    serializer_class = RedeemSerializer
    queryset = Redeem.objects.all()

    def perform_create(self, serializer):
        serializer.save(redeemed_by=self.request.user,coupon=get_object_or_404(Coupon,code=self.kwargs['code']))