from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField, PositiveIntegerField, TextField
from authentication.models import User, Store
from django.utils.translation import gettext_lazy as _

def upload_to(instance, filename):
    return 'products/{filename}'.format(filename=filename)

class Tag(models.Model):
    description = models.CharField(max_length=50, blank=False, null=False, unique=True)

    def __str__(self):
        return self.description

class Category(models.Model):
    description = models.CharField(max_length=30, null=False, blank=False, unique=True)
    rating = models.PositiveIntegerField(default=0)
    rating_num = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.description


class Type(models.Model):
    code = CharField(max_length=4, null=False, blank=False)
    title = CharField(max_length=20, null=False, blank=False)
    description = TextField(null=False, blank=False)

    def __str__(self):
        return self.title

class Product(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, null=False, default='')
    rating_num = models.PositiveIntegerField(default=0)
    overall_rating = models.PositiveIntegerField(default=0)
    price_per_unit = models.PositiveIntegerField()
    image = models.ImageField(_("image"), 
    upload_to=upload_to, null=True)
    discount = models.PositiveIntegerField(default=0)
    initial_quantity = models.PositiveBigIntegerField()
    sold_quantity = models.PositiveBigIntegerField(default=0)
    quantity = models.PositiveBigIntegerField(default=0)
    tags = models.ManyToManyField(Tag)
    categories = models.ManyToManyField(Category)
    type = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Buy_Later_Items(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False)


class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False)
    place_at = models.DateTimeField(null=True)
    checked_out_at = models.DateTimeField(null=True)
    accep_reject_at = models.DateTimeField(null=True)
    delivered_at = models.DateTimeField(null=True)
    quantity = models.IntegerField(null=False)
    price_per_unit = models.PositiveIntegerField()
    state = models.CharField(max_length=10, null=False, blank=False)


class Sales(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, null=True)
    buyer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    sale_date = models.DateTimeField(null=False)
    quantity = models.IntegerField(null=False)
    price_per_unit = models.DecimalField(max_digits=15, decimal_places=2)
    state = models.CharField(max_length=10, null=False, blank=False)


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating_number = models.PositiveIntegerField(default=0)
    review = models.TextField(null=True)
    user_name = models.CharField(max_length=100, null=True)
    date_time = models.DateTimeField(null=True)