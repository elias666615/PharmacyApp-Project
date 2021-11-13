from django.db.models import fields
from rest_framework import serializers
from .models import Product, SubCategory, Tag, Category

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'store', 'name', 'description', 'rating', 'rating_num', 'price_per_unit', 'image', 'discount', 'initial_quantity', 'sold_quantity', 'tags', 'categories']
        depth = 1

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