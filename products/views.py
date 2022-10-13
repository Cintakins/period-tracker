
from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Product, Category
from django.contrib import messages
from django.db.models import Q
from .forms import ProductForm
from django.contrib.auth.decorators import login_required

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
                price_sort = sort

            products = products.order_by(price_sort)
    context = {
        'products': products,
        'searched_item': search_query,
        'product_categories': categories,
        'direction': direction,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):

    """
    Displays single product and full description
    """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ adds articles to database """

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            product = form.save()
            messages.success(request, 'Product added!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please check over your inputs.')
    else:
        form = ProductForm()

    context = {
        'form': form,
    }

    return render(request, 'products/add_product.html', context)


@login_required
def edit_product(request, product_id):
    """ adds articles to database """

    # if not super user etc. etc.
    product = get_object_or_404(Product, pk=product_id)
    form = ProductForm(instance=product)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product Updated')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to edit product. Please check over your inputs.')
    else:
        form = ProductForm(instance=product)

    context = {
        'form': form,
        'product': product,
    }

    return render(request, 'products/edit_product.html', context)


@login_required
def delete_product(request, product_id):
    """ adds products to database """
    
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted')

    return redirect(reverse('products'))

