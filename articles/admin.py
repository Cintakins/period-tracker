from django.contrib import admin
from .models import Article, ArticleCategory

class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name'
    )
class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'title',
        'article',
        'author',
        'date_added',
    )

admin.site.register(Article)
admin.site.register(ArticleCategory)
