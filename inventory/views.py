from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import ProductSerializer, TransactionSerializer, SoldProductSerializer
from .models import Product, Category, Transaction, SoldProduct
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser

class ProductViewSet(viewsets.ModelViewSet):
  permission_classes = (IsAuthenticated,)
  serializer_class = ProductSerializer
  queryset = Product.objects.all()
  parser_classes = (MultiPartParser, FormParser)

  def create(self, request, *args, **kwargs):
    serializer = ProductSerializer(data=request.data)
    print(request.data)
    category, created = Category.objects.get_or_create(name=request.data['category'])
    request.data['category'] = category.id
    if serializer.is_valid():
      serializer.save()
      return Response({'response': 'saved'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TransactionViewSet(viewsets.ModelViewSet):
  permission_classes = (IsAuthenticated,)
  serializer_class = TransactionSerializer
  queryset = Transaction.objects.all()

class SoldProductViewSet(viewsets.ModelViewSet):
  permission_classes = (IsAuthenticated,)
  serializer_class = SoldProductSerializer
  queryset = SoldProduct.objects.all()