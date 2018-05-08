from . import views
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^v1/songs/$', views.songs_json),
    url(r'^v1/songs/(?P<pk>[0-9]+)/$', views.song_detail_json),
    url(r'^v1/songs/recommendations/(?P<pk>[0-9]+)/$', views.get_recommendations_for_song),
    url(r'^v1/images/$', views.images_json),
    url(r'^v1/images/(?P<pk>[0-9]+)/$', views.image_detail_json),
    url(r'^v1/images/recommendations/(?P<pk>[0-9]+)/$', views.get_recommendations_for_image),
    url(r'^v1/stories/$', views.stories_json),
    url(r'^v1/stories/(?P<pk>[0-9]+)/$', views.story_detail_json),
    url(r'^v1/stories/recommendations/(?P<pk>[0-9]+)/$', views.get_recommendations_for_story),
    url(r'^v1/music_videos/$', views.music_videos_json),
    url(r'^v1/music_videos/(?P<pk>[0-9]+)/$', views.music_video_detail_json),
    url(r'^v1/music_videos/recommendations/(?P<pk>[0-9]+)/$', views.get_recommendations_for_music_video),
    url(r'^v1/poems/$', views.poems_json),
    url(r'^v1/poems/(?P<pk>[0-9]+)/$', views.poem_detail_json),
    url(r'^v1/poems/recommendations/(?P<pk>[0-9]+)/$', views.get_recommendations_for_poem),
    url(r'^v1/users/$', views.create_user),
    url(r'^v1/users/(?P<pk>[0-9]+)/$', views.user_detail_json),
    url(r'^v1/login/$', views.login),
    url(r'^v1/logout/$', views.logout),
    url(r'^v1/search/$', views.search)
]

urlpatterns = format_suffix_patterns(urlpatterns)
