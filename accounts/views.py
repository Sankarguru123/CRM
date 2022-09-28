from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.renderers import JSONRenderer,HTMLFormRenderer
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework import status
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import generics
# from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle, ScopedRateThrottle
from rest_framework import filters

from .serializers import ProductSerializer, OrderSerializer,CustomerSerializer
from ..models import Product,Order,Customer


class ProductAPIView(APIView):


    def get(self, request):
        product = Product.objects.all()
        serializers = ProductSerializer(product, many=True)
        return Response(serializers.data)

    def post(self, request):
        serializers = ProductSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return HttpResponse(serializers.data)
        else:
            return HttpResponse(serializers.errors)


class ProductDetailAV(APIView):
    # permission_classes = [IsAdminOrReadOnly]
    # throttle_classes = [AnonRateThrottle]

    def get(self, request, pk):
        try:
            platform = Product.objects.get(pk=pk)
        except ProductSerializer.DoesNotExist:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProductSerializer(
            platform, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        platform = Product.objects.get(pk=pk)
        serializer = ProductSerializer(platform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        platform = Product.objects.get(pk=pk)
        platform.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)




class OrderDataVS(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
