from django import forms
from .models import UserProfile
from .models import UserPeriodInfo

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
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False


class PeriodUpload(forms.ModelForm):
    user = forms.CharField()
    period_start_date = forms.DateField()
    period_length = forms.IntegerField()

    def __init__(self, *args, **kwargs):
        super(PeriodUpload, self).__init__(*args, **kwargs)
        self.fields['period_start_date'].label = 'Click to select the start date of your last period'
        self.fields['period_length'].label = 'Select the length of your last cycle'
    
    class Meta:
        model = UserPeriodInfo
        fields = '__all__'



