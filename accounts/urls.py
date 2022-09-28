from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
from .views import ProductAPIView,ProductDetailAV,OrderDataVS

router = DefaultRouter()
router.register('order', OrderDataVS, basename='Order_details')

urlpatterns = [
    path('product/', ProductAPIView.as_view(), name='product'),
    path('product/<int:pk>', ProductDetailAV.as_view(), name='product-detail'),
    path('', include(router.urls)),



]
