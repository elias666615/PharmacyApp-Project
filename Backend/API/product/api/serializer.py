from rest_framework import serializers
from product.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'rating', 'rating_num', 'price_per_unit', 'image', 'discount', 'initial_quantity', 'sold_quantity']
        depth = 1