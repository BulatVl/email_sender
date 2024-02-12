from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email_verified = models.BooleanField(default=False)
    telegram = models.CharField(max_length=30)
    telegram_verified = models.BooleanField(default=False)
    phone = models.CharField(max_length=15)
    phone_verified = models.BooleanField(default=False)
    lat = models.FloatField(null=True, blank=True)
    lon = models.FloatField(null=True, blank=True)
