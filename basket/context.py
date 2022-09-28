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

    for item_id, quantity in basket.items():
        product = get_object_or_404(Product, pk=item_id)
        item_count += quantity 
        total = quantity * product.price
        basket_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)

    grand_total = delivery + total

    context = {
        'grand_total': grand_total,
        'basket_items': basket_items,
        'item_count': item_count,
        'total': total,
        'delivery': delivery,
    }

    return context