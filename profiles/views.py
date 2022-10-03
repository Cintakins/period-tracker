from django.shortcuts import render


def profile(request):
    """ returns profile view """

    context = {}

    return render(request, 'profiles/profile.html', context)
