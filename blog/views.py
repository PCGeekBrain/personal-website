from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from datetime import datetime
from django.utils import timezone
from .misc import random_stock_image

# Create your views here.
def see_recent(request):
    posts = Post.objects.filter(publish_date__lte=timezone.now()).order_by('-publish_date').defer('content')
    return render(request, 'blog/recent.html', {"posts": posts, "stock_image": random_stock_image})

def view_post(request, path):
    post = get_object_or_404(Post, path=path)
    return render(request, 'blog/single_post.html', {"post": post, "stock_image": random_stock_image()})
