from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

USER_TYPES = ( ('mentor', 'Mentor'), ('student', 'Student'), )

class UserType(models.Model):
    type = models.CharField(max_length=20, choices=USER_TYPES)

    def __str__(self):
        return str(self.type)

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    user_type_id = models.ForeignKey(UserType, models.PROTECT, null=True , blank=True)
    phone_number = models.IntegerField( null=True, blank=True)

class Teacher(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    experties = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return str(self.user)

class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    national_code = models.DecimalField(decimal_places=0, max_digits=10, null=True, blank=True)
    mother_phone_number = models.DecimalField(decimal_places=0, max_digits=11, null=True, blank=True)
    father_phone_number = models.DecimalField(decimal_places=0, max_digits=11, null=True, blank=True)
    home_phone_number = models.DecimalField(decimal_places=0, max_digits=11, null=True, blank=True)
    city = models.CharField(max_length=100, blank=True)
    interets = models.CharField(max_length=256 ,blank=True)
    degree = models.CharField(max_length=50 ,blank=True)
    birth_date = models.DateField(null=True)

    def __str__(self):
        return str(self.user)