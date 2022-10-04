from django.contrib import admin

from .models import Order, OrderLineItem

class OrderAdmin(admin.ModelAdmin):
    readonly_fields = (
        'order_number',
        'date',
        'delivery_cost',
        'order_total',
        'grand_total',
        )

    list_display = (
        'order_number',
        'full_name',
        'date',
        'delivery_cost',
        'order_total',
        'grand_total', 
    )

    fields = (
        'order_number',
        'date', 
        'full_name',
        'email', 
        'phone_number', 
        'country',
        'postcode', 
        'town_or_city', 
        'street_address1',
        'street_address2', 
        'county', 
        'delivery_cost',
        'order_total', 
        'grand_total',
        )

class OrderLineItemAdmin(admin.ModelAdmin):
    readonly_fields = (
        'lineitem_total',
    )
    list_display = (
        'order',
        'product',
        'product_size',
        'quantity',
    )


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderLineItem, OrderLineItemAdmin)
