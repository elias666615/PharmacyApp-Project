from django.db import models
from django.db.models.fields import CharField, TextField
from authentication.models import User, Store

class Tag(models.Model):
    description = models.CharField(max_length=50, blank=False, null=False, unique=True)

    def __str__(self):
        return self.description

class Category(models.Model):
    description = models.CharField(max_length=30, null=False, blank=False, unique=True)

    def __str__(self):
        return self.description

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False)
    description = models.CharField(max_length=30, null=False, blank=False, unique=True)

    def __str__(self):
        return self.description

class Product(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=100)
    description = models.TextField()
    rating = models.FloatField(default=2.5)
    rating_num = models.PositiveIntegerField(default=0)
    price_per_unit = models.DecimalField(max_digits=15, decimal_places=2)
    image = models.ImageField(null=True)
    discount = models.FloatField(default=0.0)
    initial_quantity = models.PositiveBigIntegerField()
    sold_quantity = models.PositiveBigIntegerField(default=0)
    tags = models.ManyToManyField(Tag)
    categories = models.ManyToManyField(SubCategory)

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
