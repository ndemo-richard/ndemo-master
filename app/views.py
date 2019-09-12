from django.shortcuts import render
from blog.models import Post
from app.models import PostImage


def index(request):
    if request.method == 'GET':
        postimage = PostImage.objects.all()
        post = Post.objects.filter(status=1).order_by('-created_on')[0:3]
        return render(request, 'index.html', {'postimages':postimage,'post_list': post})



def codehub(request):
    return render(request, 'codehub.html')


def resume(request):
    return render(request, 'resume.html')
