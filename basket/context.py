from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


# code informed by boutique-ado mini project
def basket_contents(request):

    basket_items = []
    total = 0
    item_count = 0
    basket = request.session.get('basket', {})

    for item_id, quantity_data in basket.items():
        if isinstance(quantity_data, int):
            product = get_object_or_404(Product, pk=item_id)
            subtotal = quantity_data * product.price
            total += quantity_data * product.price
            item_count += quantity_data 
            basket_items.append({
                'subtotal': subtotal,
                'item_id': item_id,
                'quantity': quantity_data,
                'product': product,
            })
        else:
            product = get_object_or_404(Product, pk=item_id)
            for size, quantity in quantity_data['item_size'].items():
                subtotal = quantity_data * product.price
                total += quantity * product.price
                item_count += quantity
                basket_items.append({
                    'subtotal': subtotal,
                    'item_id': item_id,
                    'quantity': quantity_data,
                    'product': product,
                    'size': size,
                })

    if item_count == 0:
        delivery = 0
    elif item_count > 0 and item_count < 4:
        delivery = 3
    elif item_count > 3 and item_count <= 10:
        delivery = 5
    elif item_count > 10:
        delivery = 10

    grand_total = delivery + total

    context = {
        'grand_total': grand_total,
        'basket_items': basket_items,
        'item_count': item_count,
        'total': total,
        'delivery': delivery,
    }

    return context