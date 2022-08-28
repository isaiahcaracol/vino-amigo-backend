from rest_framework import serializers
from .models import Product, Transaction, SoldProduct

class ProductSerializer(serializers.ModelSerializer):
  image = serializers.ImageField(required=False)

  class Meta:
    model = Product
    fields = '__all__'

class SoldProductSerializer(serializers.ModelSerializer):
  class Meta:
    model = SoldProduct
    fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
  sold_products = SoldProductSerializer(many=True, read_only=True)

  class Meta:
    model = Transaction
    fields = '__all__'