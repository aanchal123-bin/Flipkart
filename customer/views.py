from django.shortcuts import render
from customer.models import*
from customer.serializers import*
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your view here,
class GetCustomerView(APIView):
    def get(self,request):
        instance = Customer.objects.all()
        serializers = GetCustomerSerializers(instance,many=True)
        return Response(serializers.data)
    def post(self,request):
        params = request.data
        print("data-",params)
        ser = GetCustomerSerializers(data=params)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response({"message":"save sucessfully"})   
    
class GetAddressView(APIView):
    def get(self,request):
        instance = CustomerAddress.objects.all()
        serializers = GetAddressSerializers(instance,many=True)
        return Response(serializers.data)

class CustomerDetailAddressView(APIView):
    def get(self,request,pk):
        instance = Customer.objects.filter(id = pk)
        serializers = CustomerDetailsAddress(instance,many=True)
        return Response(serializers.data)
