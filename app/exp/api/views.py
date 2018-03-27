from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from django.http import JsonResponse
from . import modelsapi
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth import hashers
# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

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
def create_user(request):
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
        hashed_pw = hashers.make_password(password)

        create_user_response = modelsapi.create_user({"first_name": first_name, "last_name": last_name, "username": username, "password": hashed_pw})

        # create_user_response = modelsapi.create_user({"first_name": "last", "last_name": "lkjlkjlj", "username": "baaahhhuuuuu", "password": "11111"})
        # return HttpResponse(json.dumps(mode))
        # return HttpResponse(json.dumps(create_user_response))
        return create_user_response
#
# @csrf_exempt
# def login(request):
#     if request.method == 'POST':
#         data = request.body  #grabs data from inputs in forms
#         str = data.decode('utf-8') #decodes bytes to strings
#         convert_to_json = json.loads(str) #convert string to json
#         username = convert_to_json['username']
#         password = convert_to_json['password']
#         userinfo = modelsapi.get_user_by_username(username)
#         # userjson = userinfo["results"][0]["username"]
#         if userinfo["count"] == 0:
#             return HttpResponse("NOPE")
#         if userinfo["results"][0]["username"] == username and userinfo["results"][0]["password"] == password:
#             return HttpResponse("IT WORKS!!!")
#             auth = modelsapi.create_auth(user_data["username"])
#         return HttpResponse("Password or username is incorrect")
#         # return HttpResponse(json.dumps(user_data))
#         # else:
#         #     return HttpResponse(user_data)

def user_detail_json(request, pk):
    return JsonResponse(modelsapi.get_user(pk))

@csrf_exempt
def login(request):
    if request.method == 'POST':
        post_dict = request.POST.dict()
        if modelsapi.verify_login(post_dict):
            create_auth_resp = modelsapi.create_auth(post_dict["username"])
            create_auth_resp['status_code'] = 201
            #return HttpResponse(str(create_auth_resp))
            return JsonResponse(create_auth_resp)
    resp = {'ok':False}
    return JsonResponse(resp)

def logout(request):
    authenticator = request.get_cookie('auth')
    
