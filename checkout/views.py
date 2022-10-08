from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib import messages
from django.conf import settings
import stripe
from basket.context import basket_contents
from products.models import Product
from .forms import OrderForm
from .models import OrderLineItem, Order
from django.views.decorators.http import require_POST
import json
from profiles.forms import UserForm
from profiles.models import UserProfile

@require_POST
def checkout_data_cache(request):
    try:
        p_intent_id = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(p_intent_id, metadata={
            'username': request.user,
            'save_info': request.POST.get('save_info'),
            'basket': json.dumps(request.session.get('basket', {})),
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, something went wrong \ Please try again later')
        return HttpResponse(content=e, status=400)
    print(p_intent_id)

def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == "POST":
        basket = request.session.get('basket', {})
        form_info = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'country': request.POST['country'],
        }
        order_form = OrderForm(form_info)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            p_intent_id = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = p_intent_id 
            order.original_basket = json.dumps(basket)
            order.save()
            for item_id, item_data in basket.items():
                try:
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            quantity=item_data,
                            product=product,
                        )
                        order_line_item.save()
                    else:
                        for size, quantity in item_data['item_size'].items():
                            order_line_item = OrderLineItem(
                                order=order,
                                quantity=quantity,
                                product=product,
                                product_size=size,
                            )
                            order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request, 'One of the items in the basket does not exist')
                    order.delete()
                    return redirect(reverse('view_basket'))

            request.session['save_info'] = 'save_info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error in the form, please try again')
                            
    else:
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
        
        # if request.user.is_authenticated:
        #     try:
        #         profile = UserProfile.objects.get(user=request.user)
        #         order_form = OrderForm(initial={
        #             'full_name': profile.user.get_full_name(),
        #             'email': profile.user.email,
        #             'phone_number': profile.default_phone_number,
        #             'country': profile.default_country,
        #             'postcode': profile.default_postcode,
        #             'town_or_city': profile.default_town_or_city,
        #             'street_address1': profile.default_street_address1,
        #             'street_address2': profile.default_street_address2,
        #             'county': profile.default_county,
        #         })
        #     except UserProfile.DoesNotExist:
        #         order_form = OrderForm()
        # else:
        order_form = OrderForm()

    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent['client_secret'],
    }

    return render(request, 'checkout/checkout.html', context)

def checkout_success(request, order_number):
    """ display success page """

    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        order.user_profile = profile
        order.save()

        if save_info:
            profile_data = {
                'default_phone_number': order.phone_number,
                'default_country': order.country,
                'default_postcode': order.postcode,
                'default_town_or_city': order.town_or_city,
                'default_street_address1': order.street_address1,
                'default_street_address2': order.street_address2,
                'default_county': order.county,
            }
            user_profile_form = UserForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    messages.success(request, f'Checkout was successful for order number {order_number}.\
         A confirmation email will be sent to {order.email}')
    
    if 'basket' in request.session:
        del request.session['basket']

    context = {
        'order': order,
    }

    return render(request, 'checkout/checkout_success.html', context)