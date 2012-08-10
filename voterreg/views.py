from django.shortcuts import render_to_response
from django.template import RequestContext
from turbovote import API
import forms

def register(request):
    api_errors = None
    if request.method == "GET":
        form = forms.RegistrationForm()
    else:
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            result = form.submit_to_api()
            if result["status"] == "error":
                api_errors = result["errors"]
            else:
                # TODO: redirect.
"""
{u'url': {u'password': None, u'opaque': None, u'fragment': None, u'host': u'downloads-staging.turbovote.org', u'registry': None, u'query': None, u'path': u'/pdfs/fed871f0-c51d-012f-2aae-723c91dfec9e/TurboVote%20(Adam%20Duston%20Sr.).pdf', u'scheme': u'https', u'port': 443, u'user': None}, u'status': u'ok', u'id': u'3br3rvtw3cenb'}
"""
                pass
    return render_to_response(
        "register.html",
        { "form": form,
          "api_errors": api_errors },
        context_instance=RequestContext(request))
