from django.shortcuts import render
from app.models import PostImage,Portfolio
from zinnia.models.entry import Entry


def index(request):
    if request.method == 'GET':
        postimage = PostImage.objects.all()
        content = Portfolio.objects.all().order_by('-pub')[0:3]
        post = Entry.published.all().order_by('publication_date')[0:3]
        return render(request, 'index.html', {'postimages': postimage, 'content': content, 'post_list': post})


def codehub(request):
    return render(request, 'codehub.html')


def resume(request):
    return render(request, 'resume.html')


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def portfolio(request):
    content = Portfolio.objects.all().order_by('-pub')
    return render(request, 'portfolio.html',{'content':content})
