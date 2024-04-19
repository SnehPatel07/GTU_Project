from django.db import models

# Create your models here.

class Admin_User(models.Model):
    username = models.CharField(max_length=20)
    contact = models.IntegerField(unique=True)
    email = models.CharField(max_length=20,unique=True)
    password = models.CharField(max_length=16, blank=True)
    cpassword = models.CharField(max_length=16)
