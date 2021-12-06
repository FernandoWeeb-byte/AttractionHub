from django.http.response import HttpResponse
from django.shortcuts import render
from flask.json import jsonify
from rest_framework import viewsets,views
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Attraction, Genre, Stream
import requests
from django.http import JsonResponse
from django.core import serializers
# Create your views here.

class AnimeView(APIView):
    def get(self, request):
        print(request.data)
        
        genres = request.data.getlist('genre')
        print("adicionar no banco search",genres)
        for g in genres:
            try:
                var = Genre.objects.get(title=g)
                del var
            except Exception:
                genre = Genre.objects.create(title=g)
                genre.save()
                del genre
                
        streams = request.data.getlist('stream')
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

        streams = request.data.getlist('stream')
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
                attractionType=request.data['attractionType'],
                rating=request.data['rating']
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


class SearchView(APIView):
    def get(self, request):

        title = request.data['title']
        tp = request.data['type']
        
        lista = Attraction.objects.filter(title__icontains=title)
  
        if len(lista.values()) == 0:
            print('aqui')
            print(request.data)
            r = requests.post('http://127.0.0.1:6000/search/crawler/', data={'title': title, 'type': tp} )
            lista = Attraction.objects.filter(title__icontains=title)
            print(r)

            
        print(lista.values())
        lista_final = []
        
        for x in lista.all().values():
            x['stream'] = []
            x['genre'] = []
            lista_final.append(x)

        for ind, obj in enumerate(lista.all()):
            for s in obj.stream.all().values():
                lista_final[ind]['stream'].append(s['title'])
            for s in obj.genre.all().values():
                lista_final[ind]['genre'].append(s['title'])

        return JsonResponse({'data': lista_final, 'status':200})

class DatabaseView(APIView):
    def get(self,request):
        id = request.data['id']
        att = Attraction.objects.get(id=id)
        genres = []
        for genre in att.genre.values():
            genres.append(genre['title'])
        
        streams = []
        for stream in att.stream.values():
            streams.append(stream['title'])
            
        #print(att.values())
        print(genres)
        data = {'title': att.title, 'desc': att.desc, 'urlImg': att.urlImg,
        'attractionType': att.attractionType, 'rating': att.rating, 'genre': genres,
        'stream': streams }
        return JsonResponse({'data': data, 'status': 200})