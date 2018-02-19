from . import views
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import SongCreateView, ImageCreateView, StoryCreateView, FeedbackCreateView
from .views import SongDetailsView, ImageDetailsView, StoryDetailsView, FeedbackDetailsView

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api/v1/songs/create/$', SongCreateView.as_view(), name="create"),
    url(r'^api/v1/songs/(?P<pk>[0-9]+)/$',
        SongDetailsView.as_view(), name="details"),
    url(r'^api/v1/images/create/$', ImageCreateView.as_view(), name="create"),
    url(r'^api/v1/images/(?P<pk>[0-9]+)/$',
        ImageDetailsView.as_view(), name="details"),
    url(r'^api/v1/story/create/$', StoryCreateView.as_view(), name="create"),
    url(r'^api/v1/story/(?P<pk>[0-9]+)/$',
        StoryDetailsView.as_view(), name="details"),
    url(r'^api/v1/feedback/create/$', FeedbackCreateView.as_view(), name="create"),
    url(r'^api/v1/feedback/(?P<pk>[0-9]+)/$',
        FeedbackDetailsView.as_view(), name="details"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
