from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Tag, Category, Product
from .serializers import CategorySerializer, TagSerializer, ProductSerializer


@api_view(['GET'])
def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def product_detail(request, pk):
    if request.method == 'GET':
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(product, many=False)
        return Response(serializer.data)


@api_view(['GET',])
def category_list(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        print(serializer.data)
        return Response(serializer.data)


@api_view(['GET'])
def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)

    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return Response(serializer.data)


@api_view(['GET',])
def tag_list(request):
    if request.method == 'GET':
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        print(serializer.data)
        return Response(serializer.data)


@api_view(['GET'])
def tag_detail(request, pk):
    tag = get_object_or_404(Tag, pk=pk)

    if request.method == 'GET':
        serializer = TagSerializer(tag)
        return Response(serializer.data)