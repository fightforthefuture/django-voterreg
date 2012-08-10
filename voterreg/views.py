from django.shortcuts import render_to_response
from django.template import RequestContext
from turbovote import API
import forms

def register(request):
    form = forms.RegistrationForm()
    return render_to_response(
        "register.html",
        { "form": form },
        context_instance=RequestContext(request))

def register_ajax(request):
    pass
