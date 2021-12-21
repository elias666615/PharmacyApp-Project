from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Orders, Product, Rating, Tag, Category, Type

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'store', 'name', 'description', 'overall_rating', 'rating_num', 'price_per_unit', 'image', 'discount', 'quantity', 'initial_quantity', 'sold_quantity', 'tags', 'categories', 'type']
        depth = 1

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'description']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'description', 'rating']



class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ['id', 'title', 'description']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ['id', 'user', 'state', 'product', 'price_per_unit', 'quantity', 'place_at', 'checked_out_at', 'accep_reject_at', 'delivered_at']
        depth = 1


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'product', 'rating_number', 'review', 'user', 'user_name']