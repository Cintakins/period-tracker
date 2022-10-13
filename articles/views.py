from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Article, ArticleCategory
from .forms import ArticleForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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


def article_detail(request, article_id):

    """
    Displays single product and full description
    """

    article = get_object_or_404(Article, pk=article_id)

    context = {
        'article': article,
    }

    return render(request, 'articles/article_detail.html', context)

@login_required
def add_article(request):
    """ adds articles to database """

    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            article = form.save()
            messages.success(request, 'Article added!')
            return redirect(reverse('article_detail', args=[article.id]))
        else:
            messages.error(request, 'Failed to add article. Please check over your inputs.')
    else:
        form = ArticleForm()

    context = {
        'form': form,
    }

    return render(request, 'articles/add_article.html', context)


@login_required
def edit_article(request, article_id):
    """ adds articles to database """
    
    article = get_object_or_404(Article, pk=article_id)
    form = ArticleForm(instance=article)

    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            messages.success(request, 'Article Updated')
            return redirect(reverse('article_detail', args=[article.id]))
        else:
            messages.error(request, 'Failed to edit article. Please check over your inputs.')
    else:
        form = ArticleForm(instance=article)

    context = {
        'form': form,
        'article': article,
    }

    return render(request, 'articles/edit_article.html', context)


@login_required
def delete_article(request, article_id):
    """ adds articles to database """
    
    article = get_object_or_404(Article, pk=article_id)
    article.delete()
    messages.success(request, 'Product deleted')

    return redirect(reverse('articles'))

