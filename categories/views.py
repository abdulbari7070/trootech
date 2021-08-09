from django.shortcuts import render

from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from categories.serializers import ProductSerializer, CategorySerializer
from categories.models import Category, Product


# Product Views 
class ListProductsAPIView(ListAPIView):
    """This endpoint list all of the available todos from the database"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CreateProductsAPIView(CreateAPIView):
    """This endpoint allows for creation of a todo"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class UpdateProductsAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific todo by passing in the id of the todo to update"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class DeleteProductsAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific Todo from the database"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# Category Views 
class ListCategoryAPIView(ListAPIView):
    """This endpoint list all of the available todos from the database"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CreateCategoryAPIView(CreateAPIView):
    """This endpoint allows for creation of a todo"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer




# class UpdateProductsAPIView(UpdateAPIView):
#     """This endpoint allows for updating a specific todo by passing in the id of the todo to update"""
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

# class DeleteProductsAPIView(DestroyAPIView):
#     """This endpoint allows for deletion of a specific Todo from the database"""
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer