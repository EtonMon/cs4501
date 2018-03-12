from . import views
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import SongCreateView, ImageCreateView, StoryCreateView, FeedbackCreateView, Music_Video_CreateView, Poem_CreateView, CustomUserCreateView
from .views import SongDetailsView, ImageDetailsView, StoryDetailsView, FeedbackDetailsView, Music_Video_DetailsView, Poem_DetailsView, CustomUserDetailsView

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api/v1/songs/create/$', SongCreateView.as_view(), name="create_song"),
    url(r'^api/v1/songs/(?P<pk>[0-9]+)/$',
        SongDetailsView.as_view(), name="details"),
    url(r'^api/v1/songs/$', views.SongListView.as_view()),
    url(r'^api/v1/images/create/$', ImageCreateView.as_view(), name="create_image"),
    url(r'^api/v1/images/(?P<pk>[0-9]+)/$',
        ImageDetailsView.as_view(), name="details"),
    url(r'^api/v1/images/$', views.ImageListView.as_view()),
    url(r'^api/v1/story/create/$', StoryCreateView.as_view(), name="create_story"),
    url(r'^api/v1/story/(?P<pk>[0-9]+)/$',
        StoryDetailsView.as_view(), name="details"),
    url(r'^api/v1/story/$', views.Story_ListView.as_view()),
    url(r'^api/v1/feedback/create/$', FeedbackCreateView.as_view(), name="create_feedback"),
    url(r'^api/v1/feedback/(?P<pk>[0-9]+)/$',
        FeedbackDetailsView.as_view(), name="details"),
    url(r'^api/v1/music_videos/create/$', Music_Video_CreateView.as_view(), name="create_music_video"),
    url(r'^api/v1/music_videos/(?P<pk>[0-9]+)/$',
        Music_Video_DetailsView.as_view(), name="details"),
    url(r'^api/v1/music_videos/$', views.Music_Video_ListView.as_view()),
    url(r'^api/v1/poems/create/$', Poem_CreateView.as_view(), name="create_poem"),
    url(r'^api/v1/poems/(?P<pk>[0-9]+)/$',
        Poem_DetailsView.as_view(), name="details"),
    url(r'^api/v1/poems/$', views.Poem_ListView.as_view()),
    url(r'^api/v1/users/create/$', CustomUserCreateView.as_view(), name="create_user"),
    url(r'^api/v1/users/(?P<pk>[0-9]+)/$',
        CustomUserDetailsView.as_view(), name="details"),
    url(r'^api/v1/users/$',
        views.CustomUserListView.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
