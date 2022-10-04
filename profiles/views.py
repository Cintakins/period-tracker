from django.shortcuts import render, get_object_or_404
# from .models import UserProfile


def profile(request):
    """ returns profile view """
    # profile = get_object_or_404(UserProfile, user=request.user)

    context = {
    }

    return render(request, 'profiles/profile.html', context)


def account_details(request):
    """ returns account details view """

    context = {}

    return render(request, 'profiles/account_details.html', context)
