"""Handle rendering the views for the various parts of the portfolio"""
from django.shortcuts import render, get_object_or_404
from .models import Project

# Create your views here.
def single_project(request, name):
    """Return the page for a single project"""
    project = get_object_or_404(Project, path_name=name)

    return render(request, 'portfolio/single_project.html', {"project": project})
