from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Genre, Attraction, Stream
import authentication.models as am 
from rest_framework.exceptions import AuthenticationFailed
import jwt
from django.http import JsonResponse

def permission(token):
    if not token:
        raise AuthenticationFailed('Unauthenticated!')

    try:
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('Unauthenticated!')
    
    user = am.User.objects.filter(id=payload['id']).first()

    return user

# Create your views here.
class AttractionView(APIView):
    def get(self,request):
        token = request.data['token']
        tp = request.data['type']
        user = permission(token)
        if tp == 'all':
            atts = user.attractions.all().values()
        else:
            atts = user.attractions.filter(attractionType=tp).values()

        return JsonResponse({"data": list(atts),'status': 200})
    
    
    def post(self, request):
        token = request.data['token']

        user = permission(token)
        #print(request.data)
        genres = request.data.getlist('genre')
        streams = request.data.getlist('stream')
        print(genres)
        print(streams)
        for g in genres:
            Genre.objects.get_or_create(title=g)
        for s in streams:
            Stream.objects.get_or_create(title=s)

        try:
            att = Attraction.objects.create(
                title=request.data['title'],
                desc=request.data['desc'],
                rating=request.data['rating'],
                urlImg=request.data['urlImg'],
                attractionType=request.data['attractionType'],
            )
        except Exception:
            att = Attraction.objects.get(title = request.data['title'])
            return JsonResponse({"msg": "add do banco!",'status':200})

        for g in genres:
            att.genre.add(g)

        for g in streams:
            att.stream.add(g)

        #print(user)
        user.attractions.add(att.id)

        return JsonResponse({"msg": "Add!",'status':200})
    
    def put(self, request):
        token = request.data['token']
        user = permission(token)
        obj = user.attractions.filter(title=request.data['title']).values()

        if len(obj) == 0:
            return  JsonResponse({"msg": "Not found!",'status': 404})
        
        for i in request.data:
            if i == 'score':
                obj.update(score=request.data['score'])
            elif i == 'status':
                obj.update(status=request.data['status'])
            elif i == 'like':
                obj.update(like=request.data['like'])

        return  JsonResponse({"msg": "updated!",'status': 200})

    def delete(self, request):
        token = request.data['token']
        user = permission(token)
        obj = user.attractions.filter(title=request.data['title'])
        if len(obj) == 0:
            return  JsonResponse({"msg": "not found",'status': 404})

        try:
            obj.delete()
        except Exception:
            return  JsonResponse({"msg": "not deleted",'status': 200})

        return  JsonResponse({"msg": "deleted!",'status': 200})
    
class DatabaseView(APIView):
    def get(self,request):
        id = request.data['id']
        att = Attraction.objects.get(id=id )
        #print(att.values())
        
        genres = []
        for genre in att.genre.values():
            genres.append(genre['title'])
        
        streams = []
        for stream in att.stream.values():
            streams.append(stream['title'])

        data = {'title':att.title, 'desc':att.desc,'urlImg':att.urlImg,
        'attractionType':att.attractionType,'rating':att.rating,'genre':genres,
        'stream': streams, 'score': att.score, 'status': att.status }
        return JsonResponse({'data': data, 'status': 200})