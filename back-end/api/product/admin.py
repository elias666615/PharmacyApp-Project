from django.contrib import admin
from .models import Product, Category, Tag, SubCategory, Orders, Sales, Type
# Register your models here.

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Orders)
admin.site.register(Sales)
admin.site.register(Type)
admin.site.register(Tag)

