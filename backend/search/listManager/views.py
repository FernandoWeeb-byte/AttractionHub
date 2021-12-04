from django.http.response import HttpResponse
from django.shortcuts import render
from flask.json import jsonify
from rest_framework import viewsets,views
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Attraction, Genre, Stream
import requests
from django.http import JsonResponse
# Create your views here.

class AnimeView(APIView):
    def get(self, request):
        print(request.data)
        
        genres = request.data.getlist('genre')
        print(genres)
        for g in genres:
            try:
                var = Genre.objects.get(title=g)
                del var
            except Exception:
                genre = Genre.objects.create(title=g)
                genre.save()
                del genre
        streams = request.data.getlist('stream')
        print(streams)
        for s in streams:
            try:
                var = Stream.objects.get(title=s)
                del var
            except Exception:
                genre = Stream.objects.create(title=s)
                genre.save()
                del genre
           
        try:
            attraction = Attraction.objects.create(
                title=request.data['title'],
                desc=request.data['desc'],
                urlImg=request.data['urlImg'],
                attractionType="anime",
                rating=request.data.getlist('rating')
            )

            for g in genres:
                g = g.strip()
                attraction.genre.add(g)
            for s in streams:
                attraction.stream.add(s)
            attraction.save()
            resp = Response(status=200)
           
        except Exception:
            resp = Response(status=404)
        
        return resp


class SerieView(APIView):
    def get(self, request):
        print("entrou serieView")
        print(request.data)

        genres = request.data.getlist('genre')

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
                title=request.data['title'],
                desc=request.data['desc'],
                urlImg=request.data['urlImg'],
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

       
        title = request.data['title']
        tp = request.data['type']
        
        lista = Attraction.objects.filter(title__icontains=title)
  
        if len(lista.values()) == 0:
            r = requests.post('http://127.0.0.1:8000/search/crawler/', data={'title': title, 'type': tp} )
            lista = Attraction.objects.filter(title__icontains=title)
            resp = Response(lista.all().values(), status=200)
            return resp
        
        ret = {'stream': [], 'genre': []}
        print(len(lista.all().values()))
        for x in lista.all().values():
            for i in x:
                ret[i] = x[i]
        print(ret)
        
        [[ret['stream'].append(s['title']) for s in x.stream.all().values()] for x in lista.all()]
        
        [[ret['genre'].append(s['title']) for s in x.genre.all().values()] for x in lista.all()]
  
        resp = JsonResponse({'data': ret, 'status':200})

        return resp