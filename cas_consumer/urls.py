from django.conf.urls import *
from django.contrib.auth.views import login, logout
from cas_consumer.views import *

urlpatterns = patterns('',
    url(r'^login/', login, name="cas_login"),
    url(r'^logout/', logout, name="cas_logout"),
)
