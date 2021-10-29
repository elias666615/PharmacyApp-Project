from rest_framework import serializers
from categories.models import Category, SubCategory

class CategroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'description']
        depth = 1


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['id', 'description', 'category']
        depth = 1