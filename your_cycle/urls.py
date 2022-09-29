from django.urls import path
from . import views

urlpatterns = [
    path('', views.your_cycle, name='your_cycle'),
]