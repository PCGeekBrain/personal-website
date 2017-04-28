from django.shortcuts import render, HttpResponse, render_to_response
from django.http import Http404, JsonResponse
from django.utils.html import strip_tags, escape
from django.core.mail import send_mail, EmailMessage
from django.template import RequestContext
from portfolio.models import Project
from blog.models import Post
from django.utils import timezone
from blog.misc import random_stock_image

# Create your views here.
def homepage(request):
    if request.path == '/mail/':
        raise Http404
    projects = Project.objects.filter(completion_date__lte=timezone.now()).order_by('-completion_date')[:3]
    posts = Post.objects.filter(publish_date__lte=timezone.now()).order_by('-publish_date').defer('content')[:3]
    context = {
        "projects": projects,
        "posts": posts,
        "stock_image": random_stock_image
    }

    return render(request, 'homepage/home.html', context)

def send_message(request):
    if request.method == 'POST':
        print(request.POST)
        name = strip_tags(escape(request.POST['name']))
        phone = strip_tags(escape(request.POST['phone']))
        email = strip_tags(escape(request.POST['email']))
        message = strip_tags(escape(request.POST['message']))
        email_to_address ='me@mendel.tech'
        email_subject = 'Mendel.Tech Contact: Message from {}'.format(name)
        email_body = 'You have received a new message from your website contact form.\n\nHere are the details:\n\nName: {}\n\nEmail: {}\n\nPhone: {}\n\nMessage:\n{}'.format(name, email, phone, message)

        final_email = EmailMessage(subject=email_subject, body=email_body, from_email='noreply@mendel.tech', to=[email_to_address], reply_to=[email])
        final_email.send()
        return JsonResponse({'status': 'Success'})
    else:
        raise Http404
