from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework.response import Response
from app.serializers import *

# Create your views here.

class Productcrud(APIView):
    def get(self,request):
        POD=Product.objects.all()
        JPOD=ProductSerializers(POD,many=True)
        return Response(JPOD.data)

    def post(self,request):
        JSO=request.data
        POD=ProductSerializers(data=JSO)
        if POD.is_valid():
            POD.save()
            return Response({"insert":"INSERTED"})
        else:
            return Response({"Not":"NOT INSERTED"})