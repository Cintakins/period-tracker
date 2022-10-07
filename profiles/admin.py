from django.contrib import admin
from .models import UserProfile, UserPeriodInfo

class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'default_phone_number',
        'default_country',
        'default_postcode',
        'default_town_or_city',
        'default_street_address1',
        'default_street_address2',
        'default_county',
    )
class UserPeriodInfoAdmin(admin.ModelAdmin):
    list_display = (
        'user,' 
        'period_start_date', 
        'period_length',
    )

admin.site.register(UserProfile)
admin.site.register(UserPeriodInfo)
