from django.contrib import admin

from .models import Product, Category, Transaction, SoldProduct

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Transaction)
admin.site.register(SoldProduct)