from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import UserProfile, UserPeriodInfo
from .forms import UserForm, PeriodUpload
from django.contrib import messages
from checkout.models import Order
import datetime
from products.models import Product, Category
from articles.models import Article, ArticleCategory


def profile(request):
    """ returns profile view """

    cycle_phases = Article.objects.filter(category=1)

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
        form = PeriodUpload(instance=period_details)

    start_date = period_details.period_start_date
    today = datetime.date.today()
    

    def numOfDays(date1, date2):
        return (date2-date1).days

    cycle_day = numOfDays(start_date, today)

    length = int(period_details.period_length)

    if cycle_day > length:
        user.period_start_date = today
        user.save()

    count = 0
    days = []
    while count <= length:
        count += 1
        days.append(int(count))
        if days == length:
            break
    days.pop()
    
    span_width = 100 / length
    ovulation = length - 14
    mid_follicular = ((ovulation - 5) / 2) + 5
    mid_luteal = ovulation + 7

    context = {
        'cycle_phases': cycle_phases,
        'period_details': period_details,
        'user': user,
        'form': form,
        'days': days,
        'span_width': span_width,
        'ovulation': ovulation,
        'mid_follicular': mid_follicular,
        'mid_luteal': mid_luteal,
        'cycle_day': cycle_day,
    }

    return render(request, 'profiles/profile.html', context)


def account_details(request):
    """ returns account details view """
    profile = get_object_or_404(UserProfile, user=request.user)
    orders = profile.orders.all()
    form = UserForm(instance=profile)
    if request.method == 'POST':
      form = UserForm(request.POST, instance=profile)
      if form.is_valid():
          form.save()
          messages.success(request, 'Profile Updated')
    context = {
        'form': form,
        'orders': orders,
    }

    return render(request, 'profiles/account_details.html', context)

def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)
    # direct to checkout success via info buttons on past order list in account details

def site_management(request):
    """ returns account details view """

    return render(request, 'profiles/site_management.html')

