from django.shortcuts import render
from rest_framework import viewsets,views
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

class ManagerView(APIView):
    def get(self, request):
        print(request.data)
        return Response(status=200)