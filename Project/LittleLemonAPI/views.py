from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.permissions import BasePermission, IsAuthenticated
# Create your views here.




class CustomerName(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        customers = Customers.objects.all()

        if request.accepted_renderer.format == 'json':
            serializer = CustmoerSerializers(customers, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        elif request.accepted_renderer.format == 'html' or request.accepted_renderer.format == '*/*':
            return render(request, 'customers.html', {'customers': customers})
        
        serializer = CustmoerSerializers(customers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    


class CategoryView(APIView):
    def get(request, *args, **kwargs):
        content = Category.objects.all()
        serializer = CategorySerializers(content, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class IsManagerUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.profile.role == 'manager'


class ProductList(APIView):   
    permission_classes = [IsAuthenticated]
    
    def get(self, *args, **kwargs):
        content = Product.objects.all()
        serializer = ProductSerializers(content, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        if request.user.profile.role != 'manager':
            return Response({'detail': 'You do not have permission to perform this actionssssssss.'}, status=status.HTTP_403_FORBIDDEN)


        serializer = ProductSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializers.error, status=status.HTTP_400_BAD_REQUEST)
    
    
    
class UpdateProduct(APIView):
    permission_classes = [IsManagerUser]
    
    def get_object(self, pk):
        return get_object_or_404(Product, pk=pk)
    
    def get(self, request, pk, *args, **kwargs):
        product = self.get_object(pk)
        serializer = ProductSerializers(product)
        return Response(serializer.data)
    
    def put(self, request, pk, *args, **kwargs):
        product = self.get_object(pk)
        serializer = ProductSerializers(product, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class OrdersViews(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        orders = Orders.objects.all()
        serializer = OrdersSerializers(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, *args, **kwargs):
        order_id = kwargs.get('pk')
        order = get_object_or_404(Orders, pk=order_id, user=request.user)
        serializer = OrdersSerializers(order, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        order_id = kwargs.get('pk')
        order = get_object_or_404(Orders, pk=order_id, user=request.user)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


class UserOrders(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        orders = Orders.objects.filter(user=request.user)
        serializer = OrdersSerializers(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        order_id = kwargs.get('pk')
        order = get_object_or_404(Orders, id=order_id, user=request.user)

        serializer = OrdersSerializers(order, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def delete(self, request, *args, **kwargs):
        order_id = kwargs.get('pk')
        order = get_object_or_404(Orders, id=order_id, user=request.user)

        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    