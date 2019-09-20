from django.db import models
from tinymce.models import HTMLField
from taggit.managers import TaggableManager
from django.contrib.auth.models import User

STATUS = (
    (0, "Drafts"),
    (1, "Publish")
)


# post --
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    pic = models.ImageField(upload_to='posts/')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = HTMLField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)

    tags = TaggableManager()

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "blog/%s/" % self.slug

# test --
class Imagee(models.Model):
    title = models.CharField(max_length=200, unique=True)
    pic = models.ImageField(upload_to='imagestes')

    def __str__(self):
        return self.title
