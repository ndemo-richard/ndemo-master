from django.shortcuts import render
from app.models import PostImage


def index(request):
    if request.method == 'GET':
        postimage = PostImage.objects.all()
        return render(request, 'index.html', {'postimages': postimage})


def codehub(request):
    return render(request, 'codehub.html')


def resume(request):
    return render(request, 'resume.html')


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def portfolio(request):
    return render(request, 'portfolio.html')
