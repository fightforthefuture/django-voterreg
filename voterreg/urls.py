from django.conf.urls.defaults import *

urlpatterns = patterns(
    "voterreg.views",
    url(r"^register", "register", name="register"))
