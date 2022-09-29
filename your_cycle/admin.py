from django.contrib import admin
from .models import Cycle


class CycleAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'article',
    )

admin.site.register(Cycle)
