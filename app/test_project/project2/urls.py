from . import views
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import SongCreateView, ImageCreateView, StoryCreateView, FeedbackCreateView, Music_Video_CreateView, Poem_CreateView, CustomUserListCreateView
from .views import SongDetailsView, ImageDetailsView, StoryDetailsView, FeedbackDetailsView, Music_Video_DetailsView, Poem_DetailsView, CustomUserDetailsView

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api/v1/songs/create/$', SongCreateView.as_view(), name="create_song"),
    url(r'^api/v1/songs/(?P<pk>[0-9]+)/$',
        SongDetailsView.as_view(), name="song_details"),
    url(r'^api/v1/songs/$', views.SongListView.as_view(), name="song_list"),
    url(r'^api/v1/images/create/$', ImageCreateView.as_view(), name="create_image"),
    url(r'^api/v1/images/(?P<pk>[0-9]+)/$',
        ImageDetailsView.as_view(), name="image_details"),
    url(r'^api/v1/images/$', views.ImageListView.as_view(), name="image_list"),
    url(r'^api/v1/story/create/$', StoryCreateView.as_view(), name="create_story"),
    url(r'^api/v1/story/(?P<pk>[0-9]+)/$',
        StoryDetailsView.as_view(), name="story_details"),
    url(r'^api/v1/story/$', views.Story_ListView.as_view(), name="story_list"),
    url(r'^api/v1/feedback/create/$', FeedbackCreateView.as_view(), name="create_feedback"),
    url(r'^api/v1/feedback/(?P<pk>[0-9]+)/$',
        FeedbackDetailsView.as_view(), name="feedback_details"),
    url(r'^api/v1/music_videos/create/$', Music_Video_CreateView.as_view(), name="create_music_video"),
    url(r'^api/v1/music_videos/(?P<pk>[0-9]+)/$',
        Music_Video_DetailsView.as_view(), name="music_video_details"),
    url(r'^api/v1/music_videos/$', views.Music_Video_ListView.as_view(), name="music_video_list"),
    url(r'^api/v1/poems/create/$', Poem_CreateView.as_view(), name="create_poem"),
    url(r'^api/v1/poems/(?P<pk>[0-9]+)/$',
        Poem_DetailsView.as_view(), name="poem_details"),
    url(r'^api/v1/poems/$', views.Poem_ListView.as_view(), name="poem_list"),
    url(r'^api/v1/users/create/$', CustomUserListCreateView.as_view(), name="create_custom_user"),
    url(r'^api/v1/users/(?P<pk>[0-9]+)/$',
        CustomUserDetailsView.as_view(), name="custom_user_details"),
    url(r'^api/v1/users/$',
        views.CustomUserListCreateView.as_view(), name="custom_user_list"),
    url(r'^api/v1/auth/$',
        views.AuthCreateView.as_view(), name = "create_authenticator"),
    url(r'^api/v1/auth/(?P<user_id>[0-9]+)/$',
        views.AuthRetrieveView.as_view(), name = "retrieve_authenticator"),
    url(r'^api/v1/auth/(?P<pk>.+)/delete$',
        views.AuthDestroyView.as_view(), name = "destroy_authenticator")
]

urlpatterns = format_suffix_patterns(urlpatterns)
