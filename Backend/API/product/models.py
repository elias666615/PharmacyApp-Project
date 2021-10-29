from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    rating = models.FloatField(default=2.5)
    rating_num = models.PositiveIntegerField(default=0)
    price_per_unit = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=False)
    discount = models.FloatField(default=0.0)
    initial_quantity = models.PositiveBigIntegerField()
    sold_quantity = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return self.name