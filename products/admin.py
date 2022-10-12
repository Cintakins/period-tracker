from django.contrib import admin
from .models import Product, Category, ProductColors

# From Boutique Ado tutorials
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'image',
    )

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

class ProductColorsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


admin.site.register(ProductColors)
admin.site.register(Category)
admin.site.register(Product)
