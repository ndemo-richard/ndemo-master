from django.urls import path, re_path
from django.views.static import serve
from django.conf import settings

from app.views import (
    index,
    codehub,
    resume,
)

urlpatterns = [
    path('', index, name='home'),
    path('codehub/', codehub, name='codehub'),
    path('resume/', resume, name='resume'),
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
