from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^home/$', views.index, name='index'),
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
]