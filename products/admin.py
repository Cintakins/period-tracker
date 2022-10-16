from django.contrib import admin
from .models import Product, Category


# From Boutique Ado tutorials
class ProductAdmin(admin.ModelAdmin):
    """ display products in admin """
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'image',
    )


class CategoryAdmin(admin.ModelAdmin):
    """ display categories in admin """
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Category)
admin.site.register(Product)
