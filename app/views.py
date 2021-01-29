import mimetypes
import os
from wsgiref.util import FileWrapper

from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.utils.encoding import smart_str

from app.models import PostImage, Portfolio, Project, Resume
from ndemo import settings
from zinnia.models.entry import Entry


def index(request):
    if request.method == 'GET':
        postimage = PostImage.objects.all()
        content = Portfolio.objects.all().order_by('-pub')[0:3]
        post = Entry.published.all().order_by('publication_date')[0:3]
        return render(request, 'index.html', {'postimages': postimage, 'content': content, 'post_list': post})


def codehub(request):
    projects = Project.objects.all()
    return render(request, 'codehub.html', {'projects': projects})


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    return render(request, 'project_detail.html', {'project': project})


def resume(request):
    if request.method == 'GET':
        resumes = Resume.objects.all()
        return render(request, 'resume.html', {'resumes': resumes})


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def portfolio(request):
    portfolios = Portfolio.objects.all().order_by('-pub')
    return render(request, 'portfolio.html', {'portfolios': portfolios})


def portfolio_detail(request,id):
    portfolio = Portfolio.objects.get(id=id)
    return render(request, 'portfolio_detail.html', {'portfolio': portfolio})
    
def handler404(request, exception, template_name="404.html"):
    response = render_to_response(template_name)
    response.status_code = 404
    return response

def handler500(request, *args, **argv):
    return render(request, '500.html', status=500)
