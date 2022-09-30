from django.shortcuts import render
from .models import Article

# Create your views here.

def your_cycle(request):
    """ displays info about menstrual cycle, personal info to users, generic to non-users """

    
    cycle_phases = Article.objects.filter(category=1)

    context = {
        'cycle_phases': cycle_phases,
    }

    return render(request, 'articles/your_cycle.html', context)

