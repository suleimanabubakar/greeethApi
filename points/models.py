from django.db import models

# Create your models here.

class Currency(models.Model):
    name = models.CharField(max_length=30,unique=True)
    abbr = models.CharField(max_length=30)

class PointToCurrency:
    points = models.IntegerField()
    currency = models.OneToOneField(Currency,on_delete=models.CASCADE,related_name="point")
    created_on = models.DateTimeField(auto_now_add=True)
