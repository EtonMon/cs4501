from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from django.http import JsonResponse
from . import modelsapi
from django.views.decorators.csrf import csrf_exempt
import json

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
        return JsonResponse(modelsapi.get_users(page))
    elif request.method == 'POST':
        data = request.body
        str = data.decode('utf-8')
        json_data = json.loads(str)
        last_name = json_data["last_name"]
        first_name = json_data["first_name"]
        username = json_data["username"]
        password = json_data["password"]

        create_user_response = modelsapi.create_user({"first_name": first_name, "last_name": last_name, "username": username, "password": password})

        # create_user_response = modelsapi.create_user({"first_name": "last", "last_name": "lkjlkjlj", "username": "baaahhhuuuuu", "password": "11111"})
        mode = modelsapi.create_auth(create_user_response["username"])
        # return HttpResponse(json.dumps(mode))
        # return HttpResponse(json.dumps(create_user_response))
        return create_user_response

def user_detail_json(request, pk):
    return JsonResponse(modelsapi.get_user(pk))
