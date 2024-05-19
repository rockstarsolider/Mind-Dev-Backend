from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    age = models.IntegerField(blank=True, null=True)
    province = models.CharField(max_length=100, blank=True)
    intro_method = models.CharField(max_length=100,blank=True)

class Teacher(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return str(self.user)

class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return str(self.user)