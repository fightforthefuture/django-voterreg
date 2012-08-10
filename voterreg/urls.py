from django.conf.urls.defaults import *

urlpatterns = patterns(
    "voterreg.views",
    url(r"^register", "register", name="register"),
    url(r"^register_ajax", "register_ajax", name="register_ajax"),)
