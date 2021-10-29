from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from rest_framework.serializers import Serializer

from .serializer import CategroySerializer, SubCategorySerializer
from categories.models import Category, SubCategory

# @api_view()
# @permission_classes([AllowAny])
# def list_categories(request):
#     print(request.query_params)
#     num = int(request.query_params['num']) * 2
#     return Response({'message': 'we received your request ', "result": num})


class CategoryViewset(viewsets.ModelViewSet):
    serializer_class = CategroySerializer

    def get_queryset(self):
        categories = Category.objects.all()
        return categories

    # def retrieve(self, request, *args, **kwargs):
    #     params = kwargs
    #     print(params['pk'])
    #     params_list = params['pk'].split('-')
    #     category = Category.objects.filter(id=params_list[0], description= params_list[1])
    #     serializer = CategroySerializer(category, many=True)
    #     return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        category_data = request.data
        print(category_data)
        new_category = Category.objects.create(description = category_data["description"])
        new_category.save()
        serializer = CategroySerializer(new_category)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        logged_in_user = request.user
        if logged_in_user == "admin":
            category = self.get_object()
            category.delete()
            return Response({"message": "item has been deleted"})
        else:
            return Response({"message": "Not allowed"})


class SubCategoryViewset(viewsets.ModelViewSet):
    serializer_class = SubCategorySerializer

    def get_queryset(self):
        sub_categories = SubCategory.objects.all()
        return sub_categories

    # def retrieve(self, request, *args, **kwargs):
    #     params = kwargs
    #     print(params['pk'])
    #     params_list = params['pk'].split('-')
    #     category = Category.objects.filter(id=params_list[0], description= params_list[1])
    #     serializer = CategroySerializer(category, many=True)
    #     return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        sub_category_data = request.data
        print(sub_category_data)
        new_category = SubCategory.objects.create(description = sub_category_data["description"], category=Category.objects.get(id=sub_category_data["category"]))
        new_category.save()
        serializer = SubCategorySerializer(new_category)
        return Response(serializer.data)

    # def destroy(self, request, *args, **kwargs):
    #     logged_in_user = request.user
    #     if logged_in_user == "admin":
    #         category = self.get_object()
    #         category.delete()
    #         return Response({"message": "item has been deleted"})
    #     else:
    #         return Response({"message": "Not allowed"})