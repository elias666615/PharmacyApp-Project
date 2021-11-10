from django.db import models
from django.db.models.base import Model
from django.db.models.expressions import F
from django.db.models.fields import CharField, NullBooleanField, TextField
from django.db.models.fields.related import OneToOneField
from userapp.models import User, Store

class Product(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=100)
    description = models.TextField()
    rating = models.FloatField(default=2.5)
    rating_num = models.PositiveIntegerField(default=0)
    price_per_unit = models.DecimalField(max_digits=15, decimal_places=2)
    image = models.ImageField(null=False)
    discount = models.FloatField(default=0.0)
    initial_quantity = models.PositiveBigIntegerField()
    sold_quantity = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return self.name


class Type(models.Model):
    code = CharField(max_length=4, null=False, blank=False)
    title = CharField(max_length=20, null=False, blank=False)
    description = TextField(null=False, blank=False)

    def __str__(self):
        return self.title


class Buy_Later_Items(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False)


class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False)
    order_date = models.DateTimeField(null=False)
    quantity = models.IntegerField(null=False)
    price_per_unit = models.DecimalField(max_digits=15, decimal_places=2)
    state = models.CharField(max_length=10, null=False, blank=False)


class Sales(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, null=True)
    buyer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    sale_date = models.DateTimeField(null=False)
    quantity = models.IntegerField(null=False)
    price_per_unit = models.DecimalField(max_digits=15, decimal_places=2)
    state = models.CharField(max_length=10, null=False, blank=False)


class Category(models.Model):
    description = models.CharField(max_length=30, null=False, blank=False, unique=True)


class SubCategory(models.Model):
    category = models.OneToOneField(Category, on_delete=models.CASCADE, null=False)
    description = models.CharField(max_length=30, null=False, blank=False, unique=True)


class Tag(models.Model):
    description = models.CharField(max_length=50, blank=False, null=False, unique=True)