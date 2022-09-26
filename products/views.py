
from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Product, Category
from django.contrib import messages
from django.db.models import Q

# Create your views here.
# used Boutique ado project to help inform this code
def products(request):

    """
    Displays all products and handles search queries
    """

    products = Product.objects.all()
    search_query = None
    categories = None
    direction = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'query' in request.GET:
            search_query = request.GET['query']
            if not search_query:
                messages.error(request, 'Oops! Search box was empty.')
                return redirect(reverse('products'))

            search_q = Q(
                description__icontains=search_query
                ) | Q(name__icontains=search_query)
            products = products.filter(search_q)

        
        if 'direction' in request.GET:
            direction = request.GET['direction']
            sort = request.GET['sort']
            if direction == 'desc':
                price_sort = f'-{sort}'
            else:
                price_sort = f'+{sort}'

        products = products.order_by(price_sort)


    context = {
        'products': products,
        'searched_item': search_query,
        'product_categories': categories,
        'direction': direction,
    }

    return render(request, 'products/products.html', context)
