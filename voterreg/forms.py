from django import forms
from django.core.validators import RegexValidator

PREFIXES = ["Mr.", "Mrs.", "Miss", "Ms."]
SUFFIXES = ["Jr.", "Sr.", "II", "III", "IV" ]
STATES = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
PARTIES = ["Democrat", "Republican", "Green", "Libertarian", "Other"]

def _choices(l):
    return [(i, i) for i in l]

class RegistrationForm(forms.Form):
    prefix = forms.ChoiceField(choices=_choices(PREFIXES))
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    suffix = forms.ChoiceField(choices=_choices(SUFFIXES))
    email = forms.EmailField()
    street = forms.CharField(max_length=120)
    city = forms.CharField(max_length=60)
    state = forms.ChoiceField(choices=_choices(STATES))
    zip = forms.CharField(
        validators=[RegexValidator(
                regex=r"\d{5}|\d{9}", 
                message="Zip codes must be five or nine digits.")])
    dob = forms.DateField()
    party = forms.ChoiceField(choices=_choices(PARTIES))
    citizen = forms.BooleanField()

