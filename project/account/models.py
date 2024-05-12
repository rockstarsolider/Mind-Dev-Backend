from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    age = models.IntegerField(blank=True, null=True)
    province = models.CharField(max_length=100, blank=True)
    intro_method = models.CharField(max_length=100,blank=True)