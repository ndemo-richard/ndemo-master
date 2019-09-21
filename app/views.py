from django.shortcuts import render
from app.models import PostImage


def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')



def codehub(request):
    return render(request, 'codehub.html')


def resume(request):
    return render(request, 'resume.html')
