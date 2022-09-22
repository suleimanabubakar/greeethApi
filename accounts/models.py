from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Sum




class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    class Meta:
        ordering = ['-pk']
    
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

    @property
    def role(self):
        return self.groups.all().first() or 'N/A'
    
    @property
    def total_trees_planted(self):
        return self.trees_planted.count() or 0

    @property
    def total_footprint(self):
        return self.footprints.all().aggregate(total=Sum('total'))['total'] or 0
    
    @property
    def total_points(self):
        return self.wallet.balance if self.wallet else 0

    
    @property
    def total_offset(self):
        return self.total_trees_planted*21

@receiver(post_save,sender=CustomUser)
def create_profile(sender,instance,created, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)

class Profile(models.Model):
    user = models.OneToOneField(CustomUser,related_name="profile",on_delete=models.CASCADE)
    is_set = models.BooleanField(default=False)
    country = models.CharField(max_length=50,null=True)
    city = models.CharField(max_length=50,null=True)
    phone_no = models.CharField(max_length=10,null=True)
    linkedin = models.URLField(null=True)
    instagram = models.URLField(null=True)
    facebook = models.URLField(null=True)
    twitter = models.URLField(null=True)
    tiktok = models.URLField(null=True)


@receiver(post_save, sender=Profile)
def update_is_set(sender, instance, created, **kwargs):
    if not created and instance.country and instance.city and not instance.is_set:
        instance.is_set = True
        instance.save()

