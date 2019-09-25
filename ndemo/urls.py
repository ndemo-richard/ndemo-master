"""ndemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include,re_path

from django.contrib.sitemaps.views import index
from django.contrib.sitemaps.views import sitemap
from ndemo.sitemaps import Static_Sitemap
from zinnia.sitemaps import AuthorSitemap
from zinnia.sitemaps import CategorySitemap
from zinnia.sitemaps import EntrySitemap
from zinnia.sitemaps import TagSitemap
from django.conf import settings
from django.views.static import serve

sitemaps = {
'static': Static_Sitemap(),
'tags': TagSitemap,
'blog': EntrySitemap,
'authors': AuthorSitemap,
'categories': CategorySitemap
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    re_path(r'^blog/', include('zinnia.urls')),
    re_path(r'^comments/', include('django_comments.urls')),
    re_path(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]
