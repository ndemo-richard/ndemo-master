from django.db import models


# post image
class PostImage(models.Model):
    image = models.ImageField(upload_to='postimage')
    title = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = "postimage"

    def __unicode__(self):
        return self.title
