from django.http import HttpResponse
from .models import Order, OrderLineItem
from products.models import Product
from profiles.models import UserProfile
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

import json
import time


# from boutique-ado project
class Stripe_Webhook_Handler:
    """ for stripe webhooks """

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """ send confirmation email """
        user_email = order.email
        title = render_to_string('checkout/checkout_emails/email_title.txt', {
            'order':order
        })
        body = render_to_string('checkout/checkout_emails/email_body.txt', {
            'order':order
        })
        send_mail(title, body, settings.DEFAULT_FROM_EMAIL, [user_email])

    def handle_event(self, event):
        """
        Handle a unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook 
        """
        intent = event.data.object
        p_intent_id = intent.id
        basket = intent.metadata.basket
        save_info = intent.metadata.save_info
        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        order_exists = False
        attempt = 1
        
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    country__iexact=shipping_details.address.country,
                    postcode__iexact=shipping_details.address.postal_code,
                    town_or_city__iexact=shipping_details.address.city,
                    street_address1__iexact=shipping_details.address.line1,
                    street_address2__iexact=shipping_details.address.line2,
                    county__iexact=shipping_details.address.state,
                    grand_total=grand_total,
                    original_basket=basket,
                    stripe_pid=p_intent_id,
                )
                order_exists = True
                break
    
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            return HttpResponse(
                    content=f'Webhook received: {event["type"]} | Verified order in database',
                    status=200)
            self._send_confirmation_email(order)
        else:
            order = None
            try:
                order = Order.objects.create(
                    full_name=shipping_details.name,
                    email=billing_details.email,
                    phone_number=shipping_details.phone,
                    country=shipping_details.address.country,
                    postcode=shipping_details.address.postal_code,
                    town_or_city=shipping_details.address.city,
                    street_address1=shipping_details.address.line1,
                    street_address2=shipping_details.address.line2,
                    county=shipping_details.address.county,
                    original_basket=basket,
                    stripe_pid=p_intent_id,
                )
                for item_id, item_data in json.loads(basket).items():
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
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(content=f'Webhook received: {event["type"]} | Error {e}',
                status=500)
        self._send_confirmation_email(order)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | success, order created in webhook',
            status=200)


    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)