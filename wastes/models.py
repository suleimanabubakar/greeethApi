from django.contrib.auth.models import *
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.gis.db import models
from accounts.models import CustomUser as User

# Create your models here.


class WasteType(models.Model):
    name = models.CharField(max_length=40,unique=True)



class RecycleWaste(models.Model):
    waste_type = models.ForeignKey(WasteType,on_delete=models.CASCADE,related_name="recycled_waste")
    quantity = models.DecimalField(max_digits=40,decimal_places=2)
    price = models.DecimalField(max_digits=40,decimal_places=2)
    location = models.PointField(geography=True,)
    created_on =  models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User,related_name="waste_recycled",on_delete=models.CASCADE)
    status = models.CharField(max_length=30,default="pending")



class WasteBid(models.Model):
    waste = models.ForeignKey(RecycleWaste,on_delete=models.CASCADE,related_name="bids")
    price = models.DecimalField(max_digits=40,decimal_places=2)
    created_on =  models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User,related_name="waste_bids",on_delete=models.CASCADE)
    status = models.CharField(max_length=30,default="pending")


class SoldWaste(models.Model):
    waste = models.OneToOneField(RecycleWaste,on_delete=models.CASCADE,related_name="sold_waste")
    price = models.DecimalField(max_digits=40,decimal_places=2)
    bid = models.ForeignKey(WasteBid,on_delete=models.CASCADE,related_name="sold_bids")
    transacted_on = models.DateTimeField(auto_now_add=True)


@receiver(post_save,sender=SoldWaste)
def sold_waste_update(sender,instance,created,*args, **kwargs):
    if created:
        waste = instance.waste
        bid = instance.bid
        # update waste to sold
        waste.status = 'sold'
        waste.save()

        # completing the bid
        bid.status = 'completed'
        bid.save()

        # declining all other bid
        waste.bids.exclude(status="declined",pk=bid.pk).update(status="declined")

        

