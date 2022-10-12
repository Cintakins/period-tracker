from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('account_details/', views.account_details, name='account_details'),
    path('management/', views.site_management, name='site_management'),
]
