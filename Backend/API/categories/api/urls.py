from django.conf.urls import url
from .views import list_categories


urlpatterns = [
    url('categories', list_categories)
]