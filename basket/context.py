from decimal import Decimal
from django.conf import settings

def basket_contents(request):

    basket_items = []
    total = 0
    item_count = 0

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