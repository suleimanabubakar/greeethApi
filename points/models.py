from django.db import models

# Create your models here.

class Currency(models.Model):
    name = models.CharField(max_length=30,unique=True)

    def __str__(self) -> str:
        return self.name

class PointToCurrency(models.Model):
    points = models.IntegerField()
    currency = models.OneToOneField(Currency,on_delete=models.CASCADE,related_name="point")
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.DateTimeField(auto_now_add=True)
