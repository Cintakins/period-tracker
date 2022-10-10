from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import UserProfile, UserPeriodInfo
# from .forms import UserForm
from django.contrib import messages
from checkout.models import Order
from .forms import PeriodUpload


def profile(request):
    """ returns profile view """
    user = get_object_or_404(UserProfile, user=request.user)
    period_details = UserPeriodInfo.objects.get(user=user)
    if request.method == "POST":
        form = PeriodUpload(request.POST, instance=period_details)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your personalised cycle has been updated')
            return redirect(reverse('profile', args=[user.id]))
        else:
            messages.error(request, 'Whoops! something went wrong')
    else:
        form = PeriodUpload(request.POST, instance=period_details)


    # length = int(period_details.period_length)
    # count = 0
    # days = []
    # while days < length:
    #     count += 1
    #     days.append(int(count))
    # print('length', length)

    context = {
        'period_details': period_details,
        'user': user,
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


# def update_cycle(request, user_profile_id):

#     user_profile = get_object_or_404(UserProfile, pk=user_profile_id)

#     if request.method == "POST":
#         form = PeriodUpload(request.POST, instance=user_profile)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Your personalised cycle has been updated')
#             return redirect(reverse('profile', args=[user_profile.id]))
#         else:
#             messages.error(request, 'Whoops! something went wrong, please fill both fields')
#     else:
#         form = PeriodUpload(request.POST, instance=user_profile)

#     print(form)

#     context = {
#         'user_profile': user_profile,
#         'form': form,
#     }

#     return render(request, 'profiles/profile.html', context)
