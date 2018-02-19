from . import views
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView, Music_Video_CreateView, Poem_CreateView
from .views import DetailsView, Music_Video_DetailsView, Poem_DetailsView

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api/v1/songs/create/$', CreateView.as_view(), name="create"),
    url(r'^api/v1/songs/(?P<pk>[0-9]+)/$',
        DetailsView.as_view(), name="details"),
    url(r'^api/v1/music_videos/create/$', Music_Video_CreateView.as_view(), name="create"),
    url(r'^api/v1/music_videos/(?P<pk>[0-9]+)/$',
        Music_Video_DetailsView.as_view(), name="details"),
    url(r'^api/v1/poems/create/$', Poem_CreateView.as_view(), name="create"),
    url(r'^api/v1/poems/(?P<pk>[0-9]+)/$',
        Poem_DetailsView.as_view(), name="details"),
]    

urlpatterns = format_suffix_patterns(urlpatterns)