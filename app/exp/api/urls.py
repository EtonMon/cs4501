from . import views
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^v1/songs/$', views.songs_json),
    url(r'^v1/songs/(?P<pk>[0-9]+)/$', views.song_detail_json),
    url(r'^v1/images/$', views.images_json),
    url(r'^v1/images/(?P<pk>[0-9]+)/$', views.image_detail_json),
    url(r'^v1/stories/$', views.stories_json),
    url(r'^v1/stories/(?P<pk>[0-9]+)/$', views.story_detail_json),
    url(r'^v1/music_videos/$', views.music_videos_json),
    url(r'^v1/music_videos/(?P<pk>[0-9]+)/$', views.music_video_detail_json),
    url(r'^v1/poems/$', views.poems_json),
    url(r'^v1/poems/(?P<pk>[0-9]+)/$', views.poem_detail_json),
    url(r'^v1/users/$', views.create_user),
    url(r'^v1/users/(?P<pk>[0-9]+)/$', views.user_detail_json),
    url(r'^v1/login/$', views.login)
]

urlpatterns = format_suffix_patterns(urlpatterns)
