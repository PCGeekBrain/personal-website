""""URL patterns for portfolio"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^type/(?P<slug>\w+)', views.project_types),
    url(r'^role/(?P<slug>\w+)', views.project_roles),
    url(r'^skill/(?P<slug>\w+)', views.project_skills),
    url(r'^client/(?P<slug>\w+)', views.project_client),
    url(r'^project/(?P<name>\w+)', views.single_project),
]
