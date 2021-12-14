from django.urls import path

from .views import OrderAPIView, ProductAPIView, CategoryAPIView, SubcategoryAPIView, TagAPIView, TypeAPIView
from django.conf.urls import url

urlpatterns = [
    url('products/', ProductAPIView.as_view()),
    url('subcategories/', SubcategoryAPIView.as_view()),
    url('categories/', CategoryAPIView.as_view()),
    url('tags/', TagAPIView.as_view()),
    url('types/', TypeAPIView.as_view()),
    url('orders/', OrderAPIView.as_view()),
]