from rest_framework import serializers
from .models import Attraction, Genre


class GenreSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Genre
        fields = ('__all__')

class AttractionSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Attraction
        fields = ('__all__')