from django.db import models
from accounts.models import CustomUser as User

from points.models import Currency

# Create your models here.

class Coupon(models.Model):
    code = models.CharField(unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    currency = models.ForeignKey(Currency,on_delete=models.CASCADE,related_name="coupons")
    user = models.ForeignKey(User,related_name="coupons",on_delete=models.CASCADE)
    points = models.IntegerField
    status = models.CharField(max_length=30,default="active")


class Redeem(models.Model):
    redeemed_by = models.ForeignKey(User,on_delete=models.CASCADE)
    redeemed_on = models.DateTimeField(auto_now_add=True)
    
