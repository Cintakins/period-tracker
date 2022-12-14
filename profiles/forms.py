from django import forms
from .models import UserProfile, UserPeriodInfo

# from boutique ado


class UserForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_country': 'Country',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County',
        }

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = placeholders.get(f'{field}')
            self.fields[field].widget.attrs['placeholder'] = placeholder


class PeriodUpload(forms.ModelForm):
    class Meta:
        model = UserPeriodInfo
        exclude = ('user',)
    def __init__(self, *args, **kwargs):
        super(PeriodUpload, self).__init__(*args, **kwargs)
        self.fields['period_length'].widget.attrs.update({'class': 'white-text'})
        self.fields['period_start_date'].widget.attrs.update({'class': 'white-text'})
