from django.db import models
from django.contrib import admin


class Category(models.Model):
    name = models.CharField(max_length=150)
    friendly_name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


@admin.display(ordering='sku')
class Product(models.Model):

    name = models.CharField(max_length=150)
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL
        )
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    sku = models.CharField(max_length=20, null=False, blank=False)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
