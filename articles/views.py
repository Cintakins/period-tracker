from django.shortcuts import render
from .models import Article, ArticleCategory
from .forms import ArticleForm

# Create your views here.

def your_cycle(request):
    """ displays info about menstrual cycle, personal info to users, generic to non-users """

    
    cycle_phases = Article.objects.filter(category=1)

    context = {
        'cycle_phases': cycle_phases,
    }

    return render(request, 'articles/your_cycle.html', context)

def articles(request):
    """ displays info about menstrual cycle, personal info to users, generic to non-users """

    
    articles = Article.objects.filter(category=2)

    context = {
        'articles': articles,
    }

    return render(request, 'articles/articles.html', context)

def product_reviews(request):
    """ displays info about menstrual cycle, personal info to users, generic to non-users """

    
    product_reviews = Article.objects.filter(category=3)

    context = {
        'product_reviews': product_reviews,
    }

    return render(request, 'articles/product_reviews.html', context)


def add_article(request):
    """ adds articles to database """

    form = ArticleForm()

    context = {
        'form': form,
    }

    return render(request, 'articles/add_article.html', context)

