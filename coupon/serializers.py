from urllib import response
from wsgiref import validate
from .models import *
from rest_framework.serializers import *
from rest_framework.response import Response
from rest_framework.status import *
from greeeth.utils import generate_coupon



class CouponCreateSerializer(ModelSerializer):
    currency_name = SerializerMethodField(read_only=True)
    class Meta:
        model = Coupon
        fields = ['currency_name','value','user','code','created_on','currency']
        read_only_fields = ['code','user']

    def get_currency_name(self,obj):
        return obj.currency.name
    
    def create(self, validated_data):
        currency = validated_data['currency']
        value = validated_data['value']
        user = validated_data['user']
        required_points = float(value) * currency.point.points
        balance = user.wallet.balance
        if required_points > balance:
            raise ValidationError({'message': 'Insufficeint Points'})
        coupon_code = generate_coupon()
        return Coupon.objects.create(**validated_data, points=required_points, code=coupon_code)



class RedeemSerializer(ModelSerializer):
    class Meta:
        model = Redeem
        fields = '__all__'
        read_only_fields = ['redeemed_by','coupon']

    def create(self,validated_data):
        if validated_data['coupon'].status != "active":
            raise ValidationError({'message':'Invalid Coupon Code'})
        return Redeem.objects.create(**validated_data)