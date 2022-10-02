from django.shortcuts import render, redirect, reverse


def view_basket(request):
    """ returns bag content view """

    return render(request, 'basket/basket.html')

# help from boutique-ado project
def add_to_basket(request, item_id):
    """ adds items to basket """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']

    basket = request.session.get('basket', {})

    if size:
        if item_id in list(basket.keys()):
            if size in basket[item_id]['item_size'].keys():
                basket[item_id]['item_size'][size] += quantity
            else:
                basket[item_id]['item_size'][size] = quantity
        else:
            basket[item_id] = {'item_size': {size: quantity}}
    else:
        if item_id in list(basket.keys()):
            basket[item_id] += quantity
        else:
            basket[item_id] = quantity
        
    request.session['basket'] = basket
    return redirect(redirect_url)

# help from boutique-ado project
def update_basket(request, item_id):
    """ updates items in basket """

    quantity = int(request.POST.get('quantity'))
    print('this is the quantity', quantity)

    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']

    basket = request.session.get('basket', {})

    if size:
        if quantity > 0:
            basket[item_id]['item_size'][size] = quantity
        else:
            del basket[item_id]['item_size'][size]
    else:
        if quantity > 0:
            basket[item_id] = quantity
        else:
            basket.pop(item_id)
        
    request.session['basket'] = basket
    return redirect(reverse('view_basket'))