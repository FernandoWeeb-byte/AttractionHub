from django.shortcuts import render
from rest_framework import viewsets,views
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Attraction, Genre
import requests
# Create your views here.

class AnimeView(APIView):
    def get(self, request):
        print(request.data)
        
        genres = request.data.getlist('Genres:')
        print(genres)
        for g in genres:
            try:
                var = Genre.objects.get(title=g)
                del var
            except Exception:
                genre = Genre.objects.create(title=g)
                genre.save()
                del genre
           
        try:
            attraction = Attraction.objects.create(
                title=request.data['jp_name'],
                desc=request.data['en_synopsis'],
                urlImg=request.data['url_image'],
                attractionType="anime",
                rating=request.data.getlist('Rating:')
            )

            for g in genres:
                g = g.strip()
                attraction.genre.add(g)
            
            attraction.save()
            resp = Response(status=200)
           
        except Exception:
            resp = Response(status=404)
        
        return resp


class SerieView(APIView):
    def get(self, request):
        print("entrou serieView")
        print(request.data)

        genres = request.data.getlist('genres')

        for g in genres:
            g = g.strip()
            try:
                var = Genre.objects.get(title=g)
                del var
            except Exception:
                genre = Genre.objects.create(title=g)
                genre.save()
                del genre

        try:
            attraction = Attraction.objects.create(
                title=request.data['en_name'],
                desc=request.data['desc'],
                urlImg=request.data['url_img'],
                attractionType="serie",
                rating=request.data['rating']
            )
            
            for g in genres:
                g = g.strip()
                attraction.genre.add(g)
            
            attraction.save()

            resp = Response(status=200)
        except Exception:
            resp = Response(status=404)

        return resp


class SearchView(APIView):
    def get(self, request):

        print(request.data)
        title = request.data['title']
        tp = request.data['type']
        
        lista = Attraction.objects.filter(title__icontains=title)
        print(lista.values_list())
        print(len(lista.values()))
        if len(lista.values()) == 0:
            print('entrou no if')
            requests.post('http://127.0.0.1:8000/search/crawler/', data={'title': title, 'type': tp} )
            lista = Attraction.objects.filter(title__icontains=title)
            
        
        resp = Response(status=200)

        return resp