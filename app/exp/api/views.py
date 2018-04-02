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

def index(request):
    return HttpResponse("Exp API")

@csrf_exempt
def songs_json(request):
    if request.method == 'GET':
        page = request.GET.get('page', 1)
        return JsonResponse(modelsapi.get_songs(page))
    if request.method == 'POST':
        data = request.body
        str_data = data.decode('utf-8')
        json_data = json.loads(str_data)
        title = json_data["title"]
        artists = json_data["artists"]
        owner = json_data["owner"]
        song_json = modelsapi.add_song({"title": title, "artists": artists, "owner": owner})
        return song_json
    return JsonResponse({'ok':False})

def song_detail_json(request, pk):
    return JsonResponse(modelsapi.get_song(pk))

@csrf_exempt
def images_json(request):
    if request.method == 'GET':
        page = request.GET.get('page', 1)
        return JsonResponse(modelsapi.get_images(page))
    elif request.method == 'POST':
        data = request.body
        str_data = data.decode('utf-8')
        json_data = json.loads(str_data)
        title = json_data["title"]
        artists = json_data["artists"]
        owner = json_data["owner"]
        image_json = modelsapi.add_image({"title": title, "artists": artists, "owner": owner})
        return image_json
    return JsonResponse({'ok':False})

def image_detail_json(request, pk):
    return JsonResponse(modelsapi.get_image(pk))

@csrf_exempt
def stories_json(request):
    if request.method == 'GET':
        page = request.GET.get('page', 1)
        return JsonResponse(modelsapi.get_stories(page))
    elif request.method == 'POST':
        data = request.body
        str_data = data.decode('utf-8')
        json_data = json.loads(str_data)
        title = json_data["title"]
        artists = json_data["artists"]
        text = json_data["text"]
        owner = json_data["owner"]
        story_json = modelsapi.add_story({"title": title, "artists": artists, "owner": owner, "text": text})
        return story_json
    return JsonResponse({'ok':False})

def story_detail_json(request, pk):
    return JsonResponse(modelsapi.get_story(pk))

def music_videos_json(request):
    if request.method == 'GET':
        page = request.GET.get('page', 1)
        return JsonResponse(modelsapi.get_music_videos(page))
    elif request.method == 'POST':
        post_dict = request.POST.dict()
        return JsonResponse(modelsapi.create_music_video(post_dict))
    return JsonResponse({'ok':False})

def music_video_detail_json(request, pk):
    return JsonResponse(modelsapi.get_music_video(pk))

@csrf_exempt
def poems_json(request):
    if request.method == 'GET':
        page = request.GET.get('page', 1)
        return JsonResponse(modelsapi.get_poems(page))
    elif request.method == 'POST':
        data = request.body
        str_data = data.decode('utf-8')
        json_data = json.loads(str_data)
        title = json_data["title"]
        artists = json_data["artists"]
        text = json_data["text"]
        owner = json_data["owner"]
        image_json = modelsapi.add_poem({"title": title, "artists": artists, "owner": owner, "text": text})
        return image_json
    return JsonResponse({'ok':False})

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
        db_user = modelsapi.get_user_by_username(username)
        if db_user["results"]:
            return JsonResponse({'user_in_db':True})
        create_user_response = modelsapi.create_user({"first_name": first_name, "last_name": last_name, "username": username, "password": hashed_pw})
        return create_user_response

def user_detail_json(request, pk):
    return JsonResponse(modelsapi.get_user(pk))

@csrf_exempt
def login(request):
    if request.method == 'POST':
        post_dict = request.POST.dict()
        if modelsapi.verify_login(post_dict):
            create_auth_resp = modelsapi.create_auth(post_dict["username"])
            create_auth_resp['status_code'] = 201
            return JsonResponse(create_auth_resp)
    resp = {'ok':False}
    return JsonResponse(resp)

@csrf_exempt
def logout(request):
    post_dict = request.POST.dict()
    return JsonResponse(modelsapi.delete_auth(post_dict['auth']))

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

# @csrf_exempt
# def create_song(request):
#     data = request.body
#     str_data = data.decode('utf-8')
#     json_data = json.loads(str_data)
#     title = json_data["title"]
#     artists = json_data["artists"]
#     owner = json_data["owner"]
#     song_json = modelsapi.add_song({"title": title, "artists": artists, "owner": owner})
#     return song_json

# @csrf_exempt
# def create_image(request):
#     data = request.body
#     str_data = data.decode('utf-8')
#     json_data = json.loads(str_data)
#     title = json_data["title"]
#     artists = json_data["artists"]
#     owner = json_data["owner"]
#     image_json = modelsapi.add_image({"title": title, "artists": artists, "owner": owner})
#     return image_json

# @csrf_exempt
# def create_poem(request):
#     data = request.body
#     str_data = data.decode('utf-8')
#     json_data = json.loads(str_data)
#     title = json_data["title"]
#     artists = json_data["artists"]
#     text = json_data["text"]
#     owner = json_data["owner"]
#     image_json = modelsapi.add_poem({"title": title, "artists": artists, "owner": owner, "text": text})
#     return image_json
