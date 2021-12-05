from django.db import models
from django.contrib.auth.models import AbstractUser
import attractionsList.models as am
#from user.attractionsList.models import Attraction
# from ..attractionsList.models import *
# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    attractions = models.ManyToManyField(am.Attraction, blank=True)
   # USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []