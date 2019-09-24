from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class Static_Sitemap(Sitemap):
    priority = 1.0
    changefreq = 'daily'

    def items(self):
        return ['home', 'resume', 'codehub', 'about', 'contact', 'portfolio']

    def location(self, item):
        return reverse(item)

# class Article_Sitemap(Sitemap):
# priority = 0.7

#   def items(self):
#      return Article.objects.all()

# def location(self, obj):
#  return obj.note_full_path

# def lastmod(self, obj):
#   return obj.date_modified
