from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import AttractionSerializer, GenreSerializer
from .models import Genre, Attraction

# Create your views here.
class AttractionView(APIView):
    def post(self, request):
        serializer = AttractionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class GenreView(APIView):
    def post(self, request):
        serializer = GenreSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)