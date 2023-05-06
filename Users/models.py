import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver


class User(AbstractUser):
    is_Employer = models.BooleanField(default=False)
    is_Laborer = models.BooleanField(default=False)
    is_Contractor = models.BooleanField(default=False)

    def __str__(self):
        return self.email

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class Employer(models.Model):
    user = models.OneToOneField(User, related_name='Hirer', on_delete=models.CASCADE, primary_key=True)
    email = models.EmailField(max_length=100, blank=True, null=True)


    def __str__(self):
        return self.user.email


class Laborer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    email = models.EmailField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.user.email

class Contractor(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    email = models.EmailField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.user.email

"""    address = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    zip = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=10, blank=True)"""

"""   phone = models.CharField(max_length=10, blank=True)
   skills = models.CharField(max_length=100, blank=True)
   address = models.CharField(max_length=100, blank=True)
   city = models.CharField(max_length=100, blank=True)
   state = models.CharField(max_length=100, blank=True)
   zip = models.CharField(max_length=100, blank=True)"""

"""    phone = models.CharField(max_length=10, blank=True)
    skills = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    zip = models.CharField(max_length=100, blank=True)"""