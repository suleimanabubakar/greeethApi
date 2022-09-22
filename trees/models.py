from django.contrib.gis.db import models
from accounts.models import CustomUser as User
from pathlib import Path
from datetime import datetime,date
# Create your models here.


def image_location(instance,filename):
    return Path(f'plantations/{instance.planter.pk}')/filename

class Tree(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    planter = models.ForeignKey(User,related_name="trees_planted",on_delete=models.CASCADE)
    location = models.PointField(geography=True,)
    height = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to=image_location)
    tree_type = models.CharField(max_length=40,null=True)
    planted_at = models.CharField(null=True,max_length=30)


    @property
    def age(self):
        planted_on = self.created_on.date()
        now= date.today()
        return (now-planted_on).days

    @property
    def to_be_maintained(self):
        return True

    

    @property
    def address(self):
        return self.planted_at

    @property
    def humidity(self):
        return 10
    

    @property
    def temperature(self):
        return 50