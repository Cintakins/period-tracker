from django.shortcuts import render
from .models import Cycle

# Create your views here.

def your_cycle(request):
    """ displays info about menstrual cycle, personal info to users, generic to non-users """

    cycles = Cycle.objects.all()

    context = {
        'cycles': cycles,
    }

    return render(request, 'your_cycle/your_cycle.html', context)