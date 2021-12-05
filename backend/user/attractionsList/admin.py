from django.contrib import admin

from .models import Genre, Attraction, Stream

# Register your models here.
admin.site.register(Genre)
admin.site.register(Stream)
admin.site.register(Attraction)