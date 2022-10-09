from django.shortcuts import render, get_object_or_404
from .models import UserProfile, UserPeriodInfo
# from .forms import UserForm
# from django.contrib import messages
from checkout.models import Order


def profile(request):
    """ returns profile view """
    profile = get_object_or_404(UserProfile, user=request.user)
    period_details = UserPeriodInfo(request.user)

    context = {
        'period_details': period_details,
        'profile': profile,
    }
    if request.method == "POST":
        period_info = {
            'period_start_date': request.POST['period-start-date'],
            'period_length': request.POST['period-length'],
        }
        period_form = UserPeriodInfo(period_info)

    return render(request, 'profiles/profile.html', context)


def account_details(request):
    """ returns account details view """
    profile = get_object_or_404(UserProfile, user=request.user)
    orders = profile.orders.all()
    # form = UserForm(instance=profile)
    # if request.method == 'POST':
    #   form = UserForm(request.POST, instance=profile)
    #   if form.is_valid():
    #       form.save()
    #       messages.success(request, 'Profile Updated')
    context = {
        # 'form': form,
        'orders': orders,
    }

    return render(request, 'profiles/account_details.html', context)

def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)
    # direct to checkout success via info buttons on past order list in account details