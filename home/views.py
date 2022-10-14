from django.shortcuts import render
from articles.models import Article, ArticleCategory

# Create your views here.

def index(request):

    # latest_article = Article.objects.filter(category=2, 3)
    return render(request, 'home/index.html')
