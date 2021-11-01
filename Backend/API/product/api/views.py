from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import ProductSerializer
from product.models import Product

class ProductsAPIView(APIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        products = Product.objects.all()
        return products

    def get(self, request, *args, **kwargs):
        try:
            id = request.query_params['id']
            if id != None:
                product = Product.objects.get(id=id)
                serializer = ProductSerializer(product)
        except:
            products = self.get_queryset()
            serializer = ProductSerializer(products, many=True)

        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        product_data = request.data
        print(product_data)
        discount = 0.0 if (product_data['discount'] == '' or product_data['discount'] == None) else product_data['discount']
        new_product = Product.objects.create(
            name = product_data['name'],
            description = product_data['description'],
            price_per_unit = product_data['price_per_unit'],
            image = product_data['image'],
            discount = discount,
            initial_quantity = product_data['initial_quantity'],)
        new_product.save()
        serializer = ProductSerializer(new_product)
        return Response(serializer.data)