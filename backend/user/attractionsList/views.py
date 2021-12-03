from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import AttractionSerializer
from .models import Genre, Attraction

# Create your views here.
class AttractionView(APIView):
    def post(self, request):
        genres = request.data['genre']
        for g in genres:
            try:
                var = Genre.objects.get(title=g)
                del var
            except Exception:
                genre = Genre.objects.create(title=g)
                genre.save()
                del genre
        serializer = AttractionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def put(self, request, pk):
        obj = Attraction.objects.filter(id=pk)

        if len(obj) == 0:
            return Response({"Error": "Not found!"}, status=404)
        try:
            obj.update(
            score=request.data['score'], 
            status=request.data['status'], 
            like=request.data['like']
            )
        except Exception:
            return Response({"Error": "Not updated!"}, status=404)

        return Response({"Success": "Updated!"}, status=200)

    def delete(self, request, pk):
        obj = Attraction.objects.filter(id=pk)

        if len(obj) == 0:
            return Response({"Error": "Not found!"}, status=404)

        try:
            obj.delete()
        except Exception:
            return Response({"Error": "Not deleted!"}, status=404)

        return Response({"Success": "Deleted!"}, status=200)

    
    
    