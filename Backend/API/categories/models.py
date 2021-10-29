from django.db import models
from django.db.models.deletion import CASCADE


class Category(models.Model):
    description = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.description


class SubCategory(models.Model):
    description = models.CharField(max_length=50, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.description