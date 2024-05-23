from rest_framework import serializers
from django.contrib.auth.models import User, Group
from .models import *




class CustmoerSerializers(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    class Meta:
        model = Customers
        fields = '__all__'
        
        

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'



class ProductSerializers(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    class Meta:
        model = Product
        fields = '__all__'
        
        
class Groupserializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('name',)
        
        
class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'groups')
        
        
        
class OrdersSerializers(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), write_only=True)
    product_details = ProductSerializers(source='product', read_only=True)

    class Meta:
        model = Orders
        fields = ['id', 'product', 'product_details', 'quantity']

    def create(self, validated_data):
        product = validated_data.pop('product')
        order = Orders.objects.create(product=product, **validated_data)
        return order