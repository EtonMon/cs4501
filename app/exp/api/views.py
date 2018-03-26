from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from django.http import JsonResponse
from . import modelsapi
from django.views.decorators.csrf import csrf_exempt

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

@csrf_exempt
def users_json(request):
    if request.method == 'GET':
        page = request.GET.get('page', 1)
        # create_user_response = modelsapi.create_user({"first_name": "using read", "last_name": "wtf", "username": "ihaethis", "password": "password"})
        return JsonResponse(modelsapi.get_users(page))
    elif request.method == 'POST':
        # last_name = request.POST.get('last_name','')
        # first_name = request.POST.get('first_name','')
        # username = request.POST.get('username','')
        # password = request.POST.get('password','')
        create_user_response = modelsapi.create_user({"first_name": first_name, "last_name": last_name, "username": "riri", "password": "11111"})
        # create_user_response = modelsapi.create_user({"first_name": "last", "last_name": "lkjlkjlj", "username": "riri", "password": "11111"})
        modelsapi.create_auth(create_user_response["username"])
        return create_user_response

def user_detail_json(request, pk):
    return JsonResponse(modelsapi.get_user(pk))
