from django.shortcuts import render

# Create your views here.

def view_basket(request):
    """ returns bag content view """

    return render(request, 'basket/basket.html')
