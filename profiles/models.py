from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime
from django.core.validators import MinValueValidator, MaxValueValidator


class UserProfile(models.Model):
    """ user, delivery information """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)
    default_country = CountryField(blank_label='Country *', null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_town_or_city = models.CharField(max_length=40, null=True, blank=True)
    default_street_address1 = models.CharField(max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(max_length=80, null=True, blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)

    def __str__(self):
        return self.user.username

class UserPeriodInfo(models.Model):
    """ user period information """

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    period_start_date = models.DateField(default=datetime.date.today)
    period_length = models.IntegerField(default=28, blank=True, null=True, validators=[MinValueValidator(15), MaxValueValidator(45)])

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        user_profile = UserProfile.objects.create(user=instance)
        UserPeriodInfo.objects.create(user=user_profile, period_start_date=datetime.date.today())
    
    instance.userprofile.save()