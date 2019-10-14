from django.urls import path, re_path
from django.views.static import serve
from django.conf import settings

from app.views import (
    index,
    codehub,
    project_detail,
    resume,
    contact,
    portfolio,
    portfolio_detail,
    about,
)

urlpatterns = [
    path('', index, name='home'),
    path('codehub/', codehub, name='codehub'),
    path("codehub/<int:pk>/",project_detail,name="project_detail"),
    path('resume/', resume, name='resume'),
    path('about/', about, name='about'),
    path('portfolio/', portfolio, name='portfolio'),
    path("portfolio/<int:id>/", portfolio_detail,name="portfolio_detail"),
    path('contact/', contact, name='contact'),
]

if not settings.DEBUG:
    urlpatterns += [
        re_path(r'media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        })
    ]
if settings.DEBUG:
    urlpatterns += [
        re_path(r'media/(?P<path>.*)', serve, {
            'document_root': settings.MEDIA_ROOT,
        })
    ]
