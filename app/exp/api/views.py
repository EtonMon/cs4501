from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from django.http import JsonResponse
from . import modelsapi

# Create your views here.
def index(request):
    return HttpResponse("Exp API")

def songs(request):
    page = request.GET.get('page', 1)
    return JsonResponse(modelsapi.get_songs(page))

def images(request):
    page = request.GET.get('page', 1)
    return JsonResponse(modelsapi.get_images(page))

def stories(request):
    page = request.GET.get('page', 1)
    return JsonResponse(modelsapi.get_stories(page))

def music_videos(request):
    page = request.GET.get('page', 1)
    return JsonResponse(modelsapi.get_music_videos(page))

def poems(request):
    page = request.GET.get('page', 1)
    return JsonResponse(modelsapi.get_poems(page))
