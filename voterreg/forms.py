from django import forms
from django.core.validators import RegexValidator
from django.conf import settings
from turbovote import API

PREFIXES = ["Mr.", "Mrs.", "Miss", "Ms."]
SUFFIXES = ["Jr.", "Sr.", "II", "III", "IV" ]
STATES = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
PARTIES = ["Democrat", "Republican", "Green", "Libertarian", "Other"]

SERVICE_TYPE_REGISTER_ONLY   = 1
SERVICE_TYPE_BALLOT_ONLY     = 2
SERVICE_TYPE_REGISTER_BALLOT = 3
SERVICE_TYPE_REMINDER        = 4

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
    date_of_birth = forms.DateField()
    party = forms.ChoiceField(choices=_choices(PARTIES))
    citizen = forms.BooleanField()

    def submit_to_api(self):
        api = API(settings.TURBOVOTE_API_KEY)
        c = self.cleaned_data
        return api.create(
            c["first_name"], c["last_name"], c["prefix"], c["suffix"],
            c["email"], c["street"], c["city"], c["state"], c["zip"],
            c["date_of_birth"], c["party"], c["citizen"],
            SERVICE_TYPE_REGISTER_ONLY, settings.TURBOVOTE_HOSTNAME)
