from .models import User
from rest_framework import viewsets
from rest_framework.response import Response

# Create your views here.

class UserViewSet(viewsets.ViewSet):
    def get(self, request):
        users = User.objects.all()
        return Response(data={'data': 'alo'} ,status=200)

    def post(self, request):

        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass