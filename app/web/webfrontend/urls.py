from django.conf.urls import url, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt

# from django.conf.urls import (handler400, handler403, handler404, handler500)

#
handler400 = 'views.handler400'
handler404 = 'views.handler404'
handler500 = 'views.handler500'

urlpatterns = [
    url(r'^home/$', views.index, name='index'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^songs/$', views.songs, name='songs'),
    url(r'^songs/create/$', views.create_song, name='create_song'),
    url(r'^songs/(?P<id>\d+)/$', views.SongDetailView, name='song_detail'),
    url(r'^music_videos/$', views.music_videos, name='music_videos'),
    url(r'^music_videos/create/$', views.create_music_video, name='create_music_video'),
    url(r'^music_videos/(?P<id>\d+)/$', views.MusicVideoDetailView, name='music_video_detail'),
    url(r'^stories/$', views.stories, name='stories'),
    url(r'^stories/create/$', views.create_story, name='create_story'),
    url(r'^stories/(?P<id>\d+)/$', views.StoryDetailView, name='story_detail'),
    url(r'^feedbacks/$', views.feedbacks, name='feedbacks'),
    url(r'^images/$', views.images, name='images'),
    url(r'^images/create/$', views.create_image, name='create_image'),
    url(r'^images/(?P<id>\d+)/$', views.ImageDetailView, name='image_detail'),
    url(r'^poems/$', views.poems, name='poems'),
    url(r'^poems/create/$', views.create_poem, name='create_poem'),
    url(r'^poems/(?P<id>\d+)/$', views.PoemDetailView, name='poem_detail'),
    url(r'^search/$', views.search, name='search'),
]
