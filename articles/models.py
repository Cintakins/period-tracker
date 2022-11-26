from django.db import models


class ArticleCategory(models.Model):
    name = models.CharField(max_length=100)
    friendly_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

class Article(models.Model):
    
    title = models.CharField(max_length=500)
    category = models.ForeignKey('ArticleCategory', null=True, blank=True, on_delete=models.SET_NULL)
    article = models.TextField(null=False, blank=False)
    author = models.CharField(max_length=500)
    date_added = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

