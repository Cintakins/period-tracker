from django.urls import path
from . import views

urlpatterns = [
    path('', views.your_cycle, name='your_cycle'),
    path('add_article/', views.add_article, name='add_article'),
    path('articles/', views.articles, name='articles'),
    path('product_reviews/', views.product_reviews, name='product_reviews'),
]
