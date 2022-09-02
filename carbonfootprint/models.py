from django.db import models
from accounts.models import CustomUser as User
# Create your models here.
class UserFootPrint(models.Model):
    user = models.ForeignKey(User,related_name="footprints",on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=40,decimal_places=2)
    home_emmission = models.DecimalField(max_digits=40,decimal_places=2)
    travel_emmission = models.DecimalField(max_digits=40,decimal_places=2)
    food_emmission = models.DecimalField(max_digits=40,decimal_places=2)
    secondary_emmission = models.DecimalField(max_digits=40,decimal_places=2)
    calculated_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-pk']