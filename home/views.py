from django.shortcuts import render
from articles.models import Article, ArticleCategory


def index(request):

    cycle_phases = Article.objects.filter(category=1)

    context = {
        'cycle_phases': cycle_phases,
    }

    return render(request, 'home/index.html', context)
