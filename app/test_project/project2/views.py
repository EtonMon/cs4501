# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .serializers import SongSerializer, ImageSerializer, StorySerializer, FeedbackSerializer
from .models import Song, Image, Story, Feedback
from rest_framework.documentation import include_docs_urls

def index(request):
    return HttpResponse("Hello, world.")

class SongCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Song.objects.all()
    serializer_class = SongSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()

class SongDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Song.objects.all()
    serializer_class = SongSerializer

    def delete(self, request, pk, format=None):
        song = Song.objects.get(pk=pk)
        song.delete()


class ImageCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()

class ImageDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def delete(self, request, pk, format=None):
        image = Image.objects.get(pk=pk)
        image.delete()

class StoryCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Story.objects.all()
    serializer_class = StorySerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()

class StoryDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Story.objects.all()
    serializer_class = StorySerializer

    def delete(self, request, pk, format=None):
        story = Story.objects.get(pk=pk)
        story.delete()

class FeedbackCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()

class FeedbackDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

    def delete(self, request, pk, format=None):
        feedback = Feedback.objects.get(pk=pk)
        feedback.delete()

