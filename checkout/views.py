from django.shortcuts import render, redirect, reverse
from django.contrib import messages


def checkout(request):

    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, 'There are no items in the basket')
        return redirect(reverse('products'))
    
    context = {
    }

    return render(request, 'checkout/checkout.html', context)
    
