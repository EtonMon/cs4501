from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from django.http import JsonResponse
from . import modelsapi

# Create your views here.
def index(request):
    return HttpResponse("Exp API")

def songs_json(request):
    page = request.GET.get('page', 1)
    return JsonResponse(modelsapi.get_songs(page))

def song_detail_json(request, pk):
    return JsonResponse(modelsapi.get_song(pk))

def images_json(request):
    page = request.GET.get('page', 1)
    return JsonResponse(modelsapi.get_images(page))

def image_detail_json(request, pk):
    return JsonResponse(modelsapi.get_image(pk))

def stories_json(request):
    page = request.GET.get('page', 1)
    return JsonResponse(modelsapi.get_stories(page))

def story_detail_json(request, pk):
    return JsonResponse(modelsapi.get_story(pk))

def music_videos_json(request):
    page = request.GET.get('page', 1)
    return JsonResponse(modelsapi.get_music_videos(page))

def music_video_detail_json(request, pk):
    return JsonResponse(modelsapi.get_music_video(pk))

def poems_json(request):
    page = request.GET.get('page', 1)
    return JsonResponse(modelsapi.get_poems(page))

def poem_detail_json(request, pk):
    return JsonResponse(modelsapi.get_poem(pk))
