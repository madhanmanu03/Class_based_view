from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework.response import Response
from app.serializers import *

# Create your views here.

class Productcrud(APIView):
    def get(self,request,Product_Id):
        POD=Product.objects.all()
        #POD=Product.objects.get(Product_Id=Product_Id)--->if we are giving get then we should not give many=True
        JPOD=ProductSerializers(POD,many=True)
        return Response(JPOD.data)

    def post(self,request,Product_Id):
        JSO=request.data
        POD=ProductSerializers(data=JSO)
        if POD.is_valid():
            POD.save()
            return Response({"insert":"INSERTED"})
        else:
            return Response({"Not":"NOT INSERTED"})

    def put(self,request,Product_Id):
        PO=Product.objects.get(Product_Id=Product_Id)
        PDO=ProductSerializers(PO,data=request.data)
        if PDO.is_valid():
            PDO.save()
            return Response({'update':'Data is Updated'})
        else:
            return Response({'Error':'Data is not Updated'})

    def patch(self,request,Product_Id):
        PO=Product.objects.get(Product_Id=Product_Id)
        UPDO=ProductModelSerializer(PO,data=request.data,partial=True)
        if UPDO.is_valid():
            UPDO.save()
            return Response({'update':'Data is Updated'})
        else:
            return Response({'error':'Update not done'})

    def delete(self,request,Product_Id):
        Product.objects.get(Product_Id=Product_Id).delete()
        return Response({'deletion':'Data is Deleted'})
