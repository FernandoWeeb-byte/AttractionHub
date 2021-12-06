from django.shortcuts import render
from machineLearning.mlModel import preProcess, train, predict
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
# Create your views here.


class MlView(APIView):
    def get(self,request):
        print(request.data)
        ident = request.data['title']
        print(ident)
        ret = predict(ident)
        print(ret)
        return JsonResponse({'data': ret,'status':200})

    def post(self, request): #Training
        token = request.data['token']
        print(token)
        df = preProcess(token)
        train(df)
        return JsonResponse({'data': "treinado",'status':200})

        

     