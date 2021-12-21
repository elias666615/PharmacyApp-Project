from django.contrib import admin
from .models import Product, Category, Rating, Tag, Orders, Sales, Type
# Register your models here.

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Orders)
admin.site.register(Sales)
admin.site.register(Type)
admin.site.register(Tag)
admin.site.register(Rating)

