from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import UserProfile, UserPeriodInfo
from .forms import UserForm, PeriodUpload
from django.contrib import messages
import datetime
from products.models import Product
from articles.models import Article
from django.contrib.auth.decorators import login_required


@login_required
def profile(request):
    """ returns profile view """

    cycle_phases = Article.objects.filter(category=1)
    products = Product.objects.all()
    mensis = Article.objects.filter(category__name="Mensis Phase")
    follicular = Article.objects.filter(category__name="Follicular Phase")
    ovulation_phase = Article.objects.filter(category__name="Ovulation Phase")
    luteal = Article.objects.filter(category__name="Luteal Phase")
    user = get_object_or_404(UserProfile, user=request.user)
    period_details = UserPeriodInfo.objects.get(user=user)
    form = PeriodUpload(request.POST, instance=period_details)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Your personalised cycle has been updated')
        else:
            messages.error(request, 'Whoops! something went wrong')
    else:
        form = PeriodUpload(instance=period_details)

    start_date = period_details.period_start_date
    today = datetime.date.today()

    def num_of_days(date1, date2):
        return (date2-date1).days

    cycle_day = num_of_days(start_date, today)
    length = int(period_details.period_length)

    if cycle_day > length: 
        cycle_day = num_of_days(start_date, today) % length

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
        'mensis': mensis,
        'follicular': follicular,
        'ovulation_phase': ovulation_phase,
        'luteal': luteal,
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
        'products': products,
    }

    return render(request, 'profiles/profile.html', context)


@login_required
def account_details(request):
    """ returns account details view """
    user_profile = get_object_or_404(UserProfile, user=request.user)
    orders = user_profile.orders.all()
    form = UserForm(instance=user_profile)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile Updated')
    context = {
        'form': form,
        'orders': orders,
    }

    return render(request, 'profiles/account_details.html', context)
