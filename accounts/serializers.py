from rest_framework import serializers
from ..models import Product,Order,Customer


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields= ['id','name','price','category','description','tags']
        depth=1


class OrderSerializer(serializers.ModelSerializer):

     class Meta:
         model = Order
         fields= '__all__'

class CustomerSerializer(serializers.ModelSerializer):
        class Meta:
            model = Customer
            fields= '__all__'