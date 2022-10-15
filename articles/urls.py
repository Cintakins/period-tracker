from django.urls import path
from . import views

urlpatterns = [
    path('add_article/', views.add_article, name='add_article'),
    path('articles/', views.articles, name='articles'),
    path('product_reviews/', views.product_reviews, name='product_reviews'),
    path('article_detail/<int:article_id>/', views.article_detail, name='article_detail'),
    path('edit_article/<int:article_id>/', views.edit_article, name='edit_article'),
    path('delete_article/<int:article_id>/', views.delete_article, name='delete_article'),
]
