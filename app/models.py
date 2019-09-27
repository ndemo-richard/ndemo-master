from django.db import models
from taggit.managers import TaggableManager


# post image
class PostImage(models.Model):
    image = models.ImageField(upload_to='postimage')
    title = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = "postimage"

    def __unicode__(self):
        return self.title


class Portfolio(models.Model):
    title = models.CharField(max_length=80)
    sub = models.CharField(max_length=40, null=True, blank=True)
    body = models.TextField()
    link = models.URLField(null=True, blank=True)
    pic = models.ImageField(upload_to='portfolio/')
    pub = models.DateTimeField(auto_now=False)
    draft = models.BooleanField(default=False)
    tags = TaggableManager()

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=100)
    lead = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    link = models.URLField(null=True, blank=True)
    image = models.ImageField(upload_to='project')

    class Meta:
        verbose_name = "project"

    def __unicode__(self):
        return self.title
