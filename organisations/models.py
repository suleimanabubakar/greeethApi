from django.db import models
from accounts.models import CustomUser 
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=40,unique=True)

class Organisation(models.Model):
    name = models.CharField(unique=True,max_length=40)
    address = models.CharField(max_length=30)
    created_on  = models.DateTimeField(auto_now_add=True)
    created_by  = models.ForeignKey(CustomUser,related_name="created_companies",on_delete=models.CASCADE)
    type = models.ForeignKey(Category,related_name="institutions",on_delete=models.CASCADE)

    def addUser(self,user) -> 'OrganisationOfficial':
        self.officials.create(user=user)
     
    
@receiver(post_save,sender=Organisation)
def add_official(sender,instance,created, **kwargs):
    if created:
        return instance.addOfficial(user=instance.created_by)


class OrganisationOfficial(models.Model):
    user = models.ForeignKey(CustomUser,related_name="orgs",on_delete=models.CASCADE)
    organisation = models.ForeignKey(Organisation,related_name="officials",on_delete=models.CASCADE)
    assigned_on  = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user','organisation']
