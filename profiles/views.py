from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import UserProfile, UserPeriodInfo
# from .forms import UserForm
from django.contrib import messages
from checkout.models import Order
from .forms import PeriodUpload


def profile(request):
    """ returns profile view """
    user_profile = get_object_or_404(UserProfile, user=request.user)
    redirect_url = request.POST.get('redirect_url')

    if request.method == "POST":
        form = PeriodUpload(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your personalised cycle has been updated')
            return redirect(redirect_url)
        else:
            messages.error(request, 'Whoops! something went wrong, please fill both fields')
    else:
        form = PeriodUpload(request.POST, instance=user_profile)

    period_details = UserPeriodInfo(request.user)
    context = {
        'period_details': period_details,
        'user_profile': user_profile,
        'form': form,
    }

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


# def period_form(request, user):

#     form = periodUpload(request.POST)

#     if request.method == "POST":
#         period_info = {
#             'user': user,
#             'period_start_date': request.POST.get['period-start-date'],
#             'period_length': request.POST.get['period-length'],
#         }
        
#     return render(request, 'profiles/includes/period_form.html', context)