from django.shortcuts import render
from portfolio.models import *

# Create your views here.
def homepage(request):
    projects = Project.objects.order_by('completion_date')[:3]
    context = {
        "projects": projects
    }

    return render(request, 'homepage/home.html', context)