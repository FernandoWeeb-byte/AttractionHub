from .serializers import UserSerializer
from .models import User
from rest_framework import viewsets
from rest_framework.response import Response

# Create your views here.

class UserViewSet(viewsets.ViewSet):
    def get_user(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def registration(self, request):
       serializer = UserSerializer(data=request.data)
       serializer.is_valid(raise_exception=True)
       serializer.save()
       return Response(serializer.data, status=201)

    def put(self, request):
        pass

    def delete(self, request):
        pass