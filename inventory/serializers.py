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
  sold_products = SoldProductSerializer(many=True, required=False)

  class Meta:
    model = Transaction
    fields = '__all__'

  # def create(self, validated_data):
  #   products_data = validated_data.pop('sold_products')
  #   transaction = Transaction.objects.create(**validated_data)
  #   for item in products_data:
  #     SoldProduct.objects.create(transaction, **item)
  #   return transaction