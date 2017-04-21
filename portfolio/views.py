"""Handle rendering the views for the various parts of the portfolio"""
from django.shortcuts import render, get_object_or_404
from .models import Type, Role, Skill, Client, Project
from datetime import date

# Create your views here.
def project_types(request, slug):
    """Return a list of all projects with this type"""
    project_type = get_object_or_404(Type, slug=slug)
    return render(request, 'portfolio/list.html', {"projects" : project_type.project_set.all(), "project_type": project_type.name})


def project_roles(request, slug):
    """Return a list of all projects with this role"""
    project_role = get_object_or_404(Role, slug=slug)
    return render(request, 'portfolio/list.html', {"projects" : project_role.project_set.all(), "project_type": project_role.name})


def project_skills(request, slug):
    """Return a list of all projects with this role"""
    project_skill = get_object_or_404(Skill, slug=slug)
    return render(request, 'portfolio/list.html', {"projects" : project_skill.project_set.all(), "project_type": project_skill.name})


def project_client(request, slug):
    """Return a list of all projects with this role"""
    project_client = get_object_or_404(Client, slug=slug)
    return render(request, 'portfolio/list.html', {"projects" : project_client.project_set.all(), "project_type": project_client.name})


def single_project(request, name):
    """Return the page for a single project"""
    project = get_object_or_404(Project, path_name=name)

    return render(request, 'portfolio/single_project.html', {"project": project})


def recent_projects(request):
    """Return list of recent posts"""
    projects = Project.objects.filter(completion_date__lte=date.today()).order_by('completion_date')[:10]

    return render(request, 'portfolio/recent.html', {"projects": projects})

