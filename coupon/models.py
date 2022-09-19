from django.db import models
from accounts.models import CustomUser as User
from points.models import Currency
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.contenttypes.fields import GenericForeignKey,GenericRelation

from wallet.models import Credit

# Create your models here.

class Coupon(models.Model):
    code = models.CharField(unique=True,max_length=40)
    created_on = models.DateTimeField(auto_now_add=True)
    currency = models.ForeignKey(Currency,on_delete=models.CASCADE,related_name="coupons")
    user = models.ForeignKey(User,related_name="coupons",on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=30,decimal_places=2)
    status = models.CharField(max_length=30,default="active")
    points = models.DecimalField(max_digits=30,decimal_places=2)
    credits = GenericRelation(Credit)


@receiver(post_save, sender=Coupon)
def coupon_post_save_receiver(sender,instance,created,**kwargs):
    if created:
        instance.user.wallet.create_credit(instance,instance.points)
    


class Redeem(models.Model):
    redeemed_by = models.ForeignKey(User,on_delete=models.CASCADE)
    redeemed_on = models.DateTimeField(auto_now_add=True)
    coupon = models.OneToOneField(Coupon,on_delete=models.CASCADE,related_name="redemption")
    
@receiver(post_save, sender=Redeem)
def reedeem_post_save_receiver(sender,instance,created,**kwargs):
    if created:
        instance.coupon.status = 'used'
        instance.coupon.save()