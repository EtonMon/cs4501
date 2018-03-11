from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^songs/$', views.songs, name='songs'),
    url(r'^music_videos/$', views.music_videos, name='music_videos'),
    url(r'^stories/$', views.stories, name='stories'),
    url(r'^feedbacks/$', views.feedbacks, name='feedbacks'),
    url(r'^images/$', views.images, name='images'),
    url(r'^poems/$', views.poems, name='poems'),
]