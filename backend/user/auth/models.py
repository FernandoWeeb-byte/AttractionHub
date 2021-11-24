from django.db import models


# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=30)
    username = models.CharField(max_length=15, primary_key=True)
    email = models.EmailField()
    password = models.CharField(max_length=150)