from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^project/(?P<name>\w+)', views.single_project),
]
