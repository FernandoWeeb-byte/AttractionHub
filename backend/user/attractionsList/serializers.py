from rest_framework import serializers
from .models import Attraction


class AttractionSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Attraction
        fields = ['title', 'desc', 'urlImg', 'attractionType', 'rating', 'genre']
