from django.conf.urls import include, url
# from .views import list_categories
from rest_framework.routers import DefaultRouter
from .views import CategoryViewset, SubCategoryViewset

router = DefaultRouter()
router.register('categories', CategoryViewset, basename='categories')
router.register('subcategories', SubCategoryViewset, basename='subcategories')

# urlpatterns = router.urls

urlpatterns = [
    # url('categories', list_categories),
    url('', include(router.urls))
]