from django.http import Http404

from .models import Customer, Activity, Product
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.views import APIView
from .serializers import CustomerSerializer, ProductSerializer, ActivitySerializer, ActivitySerializer_post


class CustomerDetails(viewsets.ViewSet):

    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self, pk):
        try:
            return Customer.objects.get(pk=pk)
        except Customer.DoesNotExist():
            raise Http404

    def retrieve(self, request,pk):
        customer = self.get_object(pk)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    def list(self,request):
        customer = Customer.objects.all()
        serializer = CustomerSerializer(customer,many=True)
        return Response(serializer.data)

    def put(self, request,pk):
        customer = self.get_object(pk)
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, pk, request):
        customer = self.get_object(pk)
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductDetails(viewsets.ViewSet):

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist():
            raise Http404

    def retrieve(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def list(self, request):
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)

    def put(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, pk, request):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ActivityDetails(viewsets.ViewSet):

    def post(self, request):
        serializer = ActivitySerializer_post(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self, pk):
        try:
            return Activity.objects.get(pk=pk)
        except Activity.DoesNotExist():
            raise Http404

    def retrieve(self, request,pk):
        activity = self.get_object(pk)
        serializer = ActivitySerializer(activity)
        return Response(serializer.data)

    def list(self,request):
        activity = Activity.objects.all()
        serializer = ActivitySerializer(activity,many=True)
        return Response(serializer.data)

    def put(self, request,pk):
        activity = self.get_object(pk)
        serializer = ActivitySerializer_post(activity, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        response = Response()
        response.data = {
            "message": "please enter correct id"
        }
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, pk, request):
        activity = self.get_object(pk)
        activity.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
