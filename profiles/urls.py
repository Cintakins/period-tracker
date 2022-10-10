from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('account_details/', views.account_details, name='account_details'),
    # path('update<int:user_profile_id>', views.update_cycle, name='update_cycle'),
]
