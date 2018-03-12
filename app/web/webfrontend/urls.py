from django.conf.urls import url, include
from . import views
# from django.conf.urls import (handler400, handler403, handler404, handler500)

#
handler400 = 'views.handler400'
handler404 = 'views.handler404'
handler500 = 'views.handler500'

urlpatterns = [
    url(r'^home/$', views.index, name='index'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^songs/$', views.songs, name='songs'),
    url(r'^songs/(?P<id>\d+)/$', views.SongDetailView, name='song_detail'),
    url(r'^music_videos/$', views.music_videos, name='music_videos'),
    url(r'^music_videos/(?P<id>\d+)/$', views.MusicVideoDetailView, name='music_video_detail'),
    url(r'^stories/$', views.stories, name='stories'),
    url(r'^stories/(?P<id>\d+)/$', views.StoryDetailView, name='story_detail'),
    url(r'^feedbacks/$', views.feedbacks, name='feedbacks'),
    url(r'^images/$', views.images, name='images'),
    url(r'^images/(?P<id>\d+)/$', views.ImageDetailView, name='image_detail'),
    url(r'^poems/$', views.poems, name='poems'),
    url(r'^poems/(?P<id>\d+)/$', views.PoemDetailView, name='poem_detail'),
    url(r'^search/$', views.search, name='search'),
]
