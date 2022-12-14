from django.contrib import admin

from .models import Order, OrderLineItem


class OrderLineItemAdmin(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdmin,)

    readonly_fields = (
        'order_number',
        'date',
        'delivery_cost',
        'order_total',
        'grand_total',
        'stripe_pid',
        'original_basket',
        )

    list_display = (
        'order_number',
        'user_profile',
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
        'stripe_pid',
        'original_basket',
        )


admin.site.register(Order, OrderAdmin)
