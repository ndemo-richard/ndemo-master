from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from django.utils import timezone
from taggit.models import Tag
from .models import Post, Imagee


# ======Tag Mixin View ===
class TagMixin(object):
    def get_context_data(self, **kwargs):
        context = super(TagMixin, self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context


# ===testimage==
def Imagee(request):
    content = Imagee.objects.all().order_by('-start')
    return render(request, 'index.html', {'content': content})


# ======post list view ==
class PostList(TagMixin, ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


# ====post details view ==
class PostDetails(TagMixin, DetailView):
    model = Post
    context_object_name = 'blog'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class TagPostView(TagMixin, ListView):
    template_name = 'blog/post_tag.html'
    model = Post
    paginate_by = '6'
    context_object_name = 'blog'

    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs.get('slug'))
