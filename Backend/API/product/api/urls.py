from django.conf.urls import url, include
from .views import ProductsAPIView

urlpatterns = [
    url('products', ProductsAPIView.as_view())
]