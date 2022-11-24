from .models import Article, ArticleCategory
from django import forms

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        exclude = ('date_added',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = ArticleCategory.objects.filter(name='reviews') | ArticleCategory.objects.filter(name='info')
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        self.fields['category'].choices = friendly_names
        