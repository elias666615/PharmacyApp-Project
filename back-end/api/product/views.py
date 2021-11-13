from django.shortcuts import render
from rest_framework import status
from rest_framework.serializers import Serializer
from django.db.models import Q
from authentication.models import Store
from .serializers import TagSerializer, ProductSerializer, CategorySerializer, SubCategorySerializer
from .models import Product, Tag, Category, SubCategory
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class TagAPIView(APIView):
    serializer_class = TagSerializer

    def get_queryset(self):
        tags = Tag.objects.all()
        return tags

    def get(self, request):
        tags = self.get_queryset()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        tag_data = request.data
        new_tag = Tag.objects.create(description=tag_data['description'])
        new_tag.save()
        serializer = TagSerializer(new_tag)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CategoryAPIView(APIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        categories = Category.objects.all()
        return categories

    def get(self, request):
        categories = self.get_queryset()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        category_data = request.data
        new_category = Category.objects.create(description=category_data['description'])
        new_category.save()
        serializer = CategorySerializer(new_category)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class SubcategoryAPIView(APIView):
    serializer_class = SubCategorySerializer

    def get_queryset(self):
        subcategories = SubCategory.objects.all()
        return subcategories

    def get(self, request):
        subcategories = self.get_queryset()
        serializer = SubCategorySerializer(subcategories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
    def post(self, request):
        subcategory_data = request.data
        new_subcategory = SubCategory.objects.create(category=subcategory_data['category'], description=subcategory_data['description'])
        new_subcategory.save()
        serializer = SubCategorySerializer(new_subcategory)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ProductAPIView(APIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        products = Product.objects.all()
        return products

    def get(self, request):
        try:
            store_id = request.query_params['store_id']
            print(request.query_params['store_id'])
            try:
                search = request.query_params['search']
            except:
                search = None
            if search == None or search == '':
                products = Product.objects.filter(store__id=store_id)
            else: 
                search = search.strip().lower()
                print(search)
                # products = Product.objects.filter(store__id=store_id).filter(Q(categories__description__contains = search) | Q(tags__description__contains = search) | Q(name__contains=search) | Q(store__name__contains = search))
                products = Product.objects.filter(store_id=store_id).filter(name__contains = search).order_by('initial_quantity')
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({"error":"store not found"}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        product_data = request.data
        store = Store.objects.get(id=product_data['store'])
        new_product = Product.objects.create(
            store = store,
            name = product_data['name'],
            description = product_data['description'],
            price_per_unit = product_data['price_per_unit'],
            image = product_data['image'],
            discount = product_data['discount'],
            initial_quantity = product_data['initial_quantity'],
        )

        for tag in product_data['tags']:
            tag_object = Tag.objects.get(id=tag['id'])
            new_product.tags.add(tag_object)

        for category in product_data['categories']:
            category_object = SubCategory.objects.get(id=category['id'])
            new_product.categories.add(category_object)

        new_product.save()

        serializer = ProductSerializer(new_product)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    


