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
        genres = request.data['genre']
        streams = request.data['stream']
        
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
        print(obj)
        #obj = Attraction.objects.filter(id=pk)

        if len(obj) == 0:
            return  JsonResponse({"msg": "Not found!",'status':404})
        try:
            obj.update(score=request.data['score'])
        except Exception:
            return JsonResponse({"msg": "not updated!",'status':404})
        

        return  JsonResponse({"msg": "updated!",'status':200})

    def delete(self, request, pk):
        obj = Attraction.objects.filter(id=pk)

        if len(obj) == 0:
            return Response({"Error": "Not found!"}, status=404)

        try:
            obj.delete()
        except Exception:
            return Response({"Error": "Not deleted!"}, status=404)

        return Response({"Success": "Deleted!"}, status=200)
    