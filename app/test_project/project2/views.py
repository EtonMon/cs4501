# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .serializers import SongSerializer
from .models import Song
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



