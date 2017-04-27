""""URL patterns for portfolio"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.see_recent),
]