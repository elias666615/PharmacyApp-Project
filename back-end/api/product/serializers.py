from django.db.models import fields
from rest_framework import serializers
from .models import Orders, Product, SubCategory, Tag, Category, Type

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'store', 'name', 'description', 'rating', 'rating_num', 'price_per_unit', 'image', 'discount', 'initial_quantity', 'sold_quantity', 'tags', 'categories', 'type']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'description']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'description']

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['id', 'category', 'description']


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ['id', 'title', 'description']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ['id', 'state', 'product', 'price_per_unit', 'quantity', 'order_date']
        depth = 1