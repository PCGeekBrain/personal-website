""""URL patterns for portfolio"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^mail/contact_me.php', views.send_message),
    url(r'^$', views.homepage),
]
