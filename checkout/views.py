from django.shortcuts import render, redirect, reverse
from django.contrib import messages
import stripe
from .forms import OrderForm
from basket.context import basket_contents
from django.conf import settings


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, 'There are no items in the basket')
        return redirect(reverse('products'))

    current_basket = basket_contents(request)
    total = current_basket['grand_total']
    stripe_total_int = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total_int,
        currency=settings.STRIPE_CURRENCY,
    )
    
    order_form = OrderForm()
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent['client_secret'],
    }

    return render(request, 'checkout/checkout.html', context)
    
