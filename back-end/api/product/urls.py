from django.urls import path
from .views import ProductAPIView, CategoryAPIView, SubcategoryAPIView, TagAPIView
from django.conf.urls import url

urlpatterns = [
    url('products/', ProductAPIView.as_view()),
    url('categories/', CategoryAPIView.as_view()),
    url('subcategories/', SubcategoryAPIView.as_view()),
    url('tags/', TagAPIView.as_view())
]