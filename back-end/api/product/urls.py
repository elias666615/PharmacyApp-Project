from django.urls import path

from .views import CommercialProductAPIView, OrderAPIView, ProductAPIView, CategoryAPIView, RatingAPIView, TagAPIView, TypeAPIView
from django.conf.urls import url

urlpatterns = [
    url('commercial_products/', CommercialProductAPIView.as_view()),
    url('products/', ProductAPIView.as_view()),
    url('categories/', CategoryAPIView.as_view()),
    url('tags/', TagAPIView.as_view()),
    url('types/', TypeAPIView.as_view()),
    url('orders/', OrderAPIView.as_view()),
    url('rating/', RatingAPIView.as_view()),
]