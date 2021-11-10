from django.contrib import admin
from .models import Product, Type, Orders, Sales, Category, SubCategory, Tag, Buy_Later_Items

# Register your models here.
admin.site.register(Product)
admin.site.register(Type)
admin.site.register(Orders)
admin.site.register(Sales)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Tag)
admin.site.register(Buy_Later_Items)