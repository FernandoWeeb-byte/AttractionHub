from django.db import models

# Create your models here.

class Genre(models.Model):
    title = models.CharField(max_length=64, primary_key=True)

class Stream(models.Model):
    title = models.CharField(max_length=64, primary_key=True)

class Attraction(models.Model):
    title = models.CharField(max_length=256, unique=True)
    desc = models.TextField()
    urlImg = models.URLField()
    attractionType = models.CharField(max_length=100)
    rating = models.CharField(max_length=100)
    genre = models.ManyToManyField(Genre)
    stream = models.ManyToManyField(Stream)
    score = models.PositiveIntegerField(blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    like = models.BooleanField(blank=True, null=True)
