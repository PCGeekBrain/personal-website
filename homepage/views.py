from django.shortcuts import render, HttpResponse
from django.http import Http404, JsonResponse
from django.core.mail import send_mail
from portfolio.models import *

# Create your views here.
def homepage(request):
    if request.path == '/mail/':
        raise Http404
    projects = Project.objects.order_by('completion_date')[:3]
    context = {
        "projects": projects
    }

    return render(request, 'homepage/home.html', context)


def send_message(request):
    if request.method == 'POST':
        print(request.POST)
        return JsonResponse({'status': 'Success'})
    else:
        raise Http404