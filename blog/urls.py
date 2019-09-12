from django.urls import path, re_path
from django.views.static import serve
from django.conf import settings
from blog import views

urlpatterns = [
    path('blog/', views.PostList.as_view(), name='blog'),
    path('blog/<slug:slug>/', views.PostDetails.as_view(), name='post_detail'),
    path('blog/tags/<slug:slug>', views.TagPostView.as_view(), name="tagged"),

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
