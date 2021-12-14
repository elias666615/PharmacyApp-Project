from django.shortcuts import render
from rest_framework import status
from rest_framework import serializers
from rest_framework.serializers import Serializer
from django.db.models import Q
from authentication.models import User
from authentication.models import Store
from .serializers import OrderSerializer, TagSerializer, ProductSerializer, CategorySerializer, SubCategorySerializer, TypeSerializer
from .models import Orders, Product, Tag, Category, SubCategory, Type
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser
from rest_framework import permissions
import datetime
from rest_framework.permissions import AllowAny

# Create your views here.

class TagAPIView(APIView):
    serializer_class = TagSerializer
    permission_classes = [AllowAny]

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
    permission_classes = [AllowAny]

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
    permission_classes = [AllowAny]

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

class TypeAPIView(APIView):
    serializer_class = TypeSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        types = Type.objects.all()
        return types

    def get(self, request):
        types = self.get_queryset()
        serializer = TypeSerializer(types, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class OrderAPIView(APIView):
    serializer_class = OrderSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        orders = Orders.objects.all()
        return orders
    
    def get(self, request):
        try:
            store_id = request.query_params['store']
            orders = Orders.objects.filter(product__store = store_id)
            serializer = OrderSerializer(orders, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            pass

        try:
            user_email = request.query_params['user']
            orders = Orders.objects.filter(user__email = user_email)
            serializer = OrderSerializer(orders, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            pass
        return Response({'message': 'something went wrong'}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        order_data = request.data
        product = Product.objects.get(id = order_data['product'])
        user = User.objects.get(email = order_data['user'])
        new_order = Orders.objects.create(user = user, product = product, quantity = order_data['quantity'], price_per_unit = product.price_per_unit, state = 'new', order_date = datetime.datetime.now())
        new_order.save()
        return Response({'message': 'order successfully added'}, status=status.HTTP_200_OK)

    def put(self, request):
        data = request.data
        order = Orders.objects.get(id = data['id'])
        order.state = data['state']
        order.save()
        return Response({'message': 'order successfully modified'}, status=status.HTTP_200_OK)


class ProductAPIView(APIView):
    serializer_class = ProductSerializer
    parser_classes = [FormParser, MultiPartParser]
    permission_classes = [AllowAny]

    def get_queryset(self):
        products = Product.objects.all()
        return products

    def get(self, request, format=None):

        try:
            id = request.query_params['id']
            product = Product.objects.get(id = id)
            serializer = ProductSerializer(product)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            pass

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
        print(request.data)
        product_data = request.data
        store = Store.objects.get(id=int(product_data['store']))
        type = Type.objects.get(id=int(product_data['type']))
        print('image' + str(product_data['image']))
        new_product = Product.objects.create(
            store = store,
            name = product_data['name'],
            description = product_data['description'],
            price_per_unit = float(product_data['price_per_unit']),
            image = product_data['image'],
            discount = float(product_data['discount']),
            initial_quantity = int(product_data['initial_quantity']),
            type = type
            # tags = product_data['tags'],
            # categories = product_data['categories'],
        )
        tagList = []
        for tag in product_data['tags'].split(','):
            tag = tag.strip()
            if tag == '':
                continue
            print(tag)
            tagList.append(int(tag))
        categoryList = []
        for category in product_data['categories'].split(','):
            category = category.strip()
            if category == '':
                continue
            categoryList.append(int(category))
        new_product.tags.set(tagList)
        new_product.categories.set(categoryList)

        new_product.save()

        serializer = ProductSerializer(new_product)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request):
        data = request.data
        product_object = Product.objects.get(id=int(data['id']))
    
        

        product_object.name = data['name']
        product_object.description = data['description']
        product_object.price_per_unit = data['price_per_unit']
        product_object.discount = data['discount']
        product_object.initial_quantity = data['initial_quantity']
        # product_object.image = data['image']

        tagList = []
        for tag in data['tags'].split(','):
            tag = tag.strip()
            if tag == '':
                continue
            print(tag)
            tagList.append(int(tag))
        categoryList = []
        for category in data['categories'].split(','):
            category = category.strip()
            if category == '':
                continue
            categoryList.append(int(category))

        product_object.tags.set(tagList)
        product_object.categories.set(categoryList)

        product_object.save()

        Serializer = ProductSerializer(product_object)
        return Response(Serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        id = request.query_params["id"]
        product = Product.objects.get(id=id)
        product.delete()
        return Response({'message': 'product successfully deleted'}, status=status.HTTP_200_OK)