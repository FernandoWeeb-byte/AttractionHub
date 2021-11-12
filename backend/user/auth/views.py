from django.shortcuts import render
from .models import User
from rest_framework import viewsets

# Create your views here.

class UserViewSet(viewsets.ViewSet):
    def get(self, request):
        users = User.objects.all()
        return users.values()

    def post(self, request):

        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass