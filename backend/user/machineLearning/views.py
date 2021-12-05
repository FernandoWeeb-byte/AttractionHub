from django.shortcuts import render
from machineLearning.mlModel import preProcess, train, predict
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.


class MlView(APIView):
    def get(self,request):
        ident = request.data['id']
        ret = predict(ident)
        return Response(data=ret,status=200)

    def post(self, request): #Training
        token = request.data['token']
        df = preProcess(token)
        train(df)
        return Response(status=200)

        

     