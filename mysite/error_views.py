from django.shortcuts import render, HttpResponse, render_to_response

def handle_404(request):
    return render(request, 'homepage/404.html', status=404)

def handle_500(request):
    return render(request, 'homepage/500.html', status=500)