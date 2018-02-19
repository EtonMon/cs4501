# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .serializers import SongSerializer, Music_Video_Serializer, Poem_Serializer
from .models import Song, Music_Video, Poem
from rest_framework.documentation import include_docs_urls

def index(request):
    return HttpResponse("Hello, world.")

class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Song.objects.all()
    serializer_class = SongSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Song.objects.all()
    serializer_class = SongSerializer

    def delete(self, request, pk, format=None):
        song = Song.objects.get(pk=pk)
        song.delete()

class Music_Video_CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Music_Video.objects.all()
    serializer_class = Music_Video_Serializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()

class Music_Video_DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Music_Video.objects.all()
    serializer_class = Music_Video_Serializer

    def delete(self, request, pk, format=None):
        vid = Music_Video.objects.get(pk=pk)
        vid.delete()

class Poem_CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Poem.objects.all()
    serializer_class = Poem_Serializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()

class Poem_DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Poem.objects.all()
    serializer_class = Poem_Serializer

    def delete(self, request, pk, format=None):
        poem = Poem.objects.get(pk=pk)
        poem.delete()

