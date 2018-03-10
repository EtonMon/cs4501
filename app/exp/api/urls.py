from . import views
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^v1/songs/$', views.songs),
    url(r'^v1/images/$', views.images),
    url(r'^v1/stories/$', views.stories),
    url(r'^v1/music_videos/$', views.music_videos),
    url(r'^v1/poems/$', views.poems),
]

urlpatterns = format_suffix_patterns(urlpatterns)
