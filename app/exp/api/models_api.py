import urllib.request
import urllib.parse
import json
import os
import uuid
import hmac
import requests
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import hashers
from . import kafka_api
import ast

# import django settings file
from django.conf import settings

def get_songs(page):
    # make a GET request and parse the returned JSON
    # note, no timeouts, error handling or all the other things needed to do this for real
    print ("About to perform the GET request...")
    page=page.__str__()
    req = urllib.request.Request('http://models-api:8000/project2/api/v1/songs/?page='+page)

    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    resp = json.loads(resp_json)

    print(resp)
    return resp

def get_song(pk):
    # make a GET request and parse the returned JSON
    # note, no timeouts, error handling or all the other things needed to do this for real
    print ("About to perform the GET request...")
    pk=pk.__str__()
    req = urllib.request.Request('http://models-api:8000/project2/api/v1/songs/'+pk)

    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    resp = json.loads(resp_json)

    print(resp)
    return resp

@csrf_exempt
def add_song(song_dict):
    payload = song_dict
    k = json.dumps(song_dict)
    response = requests.post('http://models-api:8000/project2/api/v1/songs/create/', data=payload)
    json_data = response.json()
    json_data['type'] = "song"
    user_data = get_user(json_data['owner'])
    json_data['username'] = user_data['username']
    kafka_api.send_to_kafka(json_data)
    return response.json()

def get_images(page):
    # make a GET request and parse the returned JSON
    # note, no timeouts, error handling or all the other things needed to do this for real
    print ("About to perform the GET request...")
    page=page.__str__()
    req = urllib.request.Request('http://models-api:8000/project2/api/v1/images/?page='+page)

    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    resp = json.loads(resp_json)

    print(resp)
    return resp

def get_image(pk):
    # make a GET request and parse the returned JSON
    # note, no timeouts, error handling or all the other things needed to do this for real
    print ("About to perform the GET request...")
    pk=pk.__str__()
    req = urllib.request.Request('http://models-api:8000/project2/api/v1/images/'+pk)

    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    resp = json.loads(resp_json)

    print(resp)
    return resp

@csrf_exempt
def add_image(image_dict):
    payload = image_dict
    response = requests.post('http://models-api:8000/project2/api/v1/images/create/', data=payload)
    json_data = response.json()
    json_data['type'] = "image"
    user_data = get_user(json_data['owner'])
    json_data['username'] = user_data['username']
    kafka_api.send_to_kafka(json_data)
    return response.json()

def get_stories(page):
    # make a GET request and parse the returned JSON
    # note, no timeouts, error handling or all the other things needed to do this for real
    print ("About to perform the GET request...")
    page=page.__str__()
    req = urllib.request.Request('http://models-api:8000/project2/api/v1/story/?page='+page)

    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    resp = json.loads(resp_json)

    print(resp)
    return resp

def get_story(pk):
    # make a GET request and parse the returned JSON
    # note, no timeouts, error handling or all the other things needed to do this for real
    print ("About to perform the GET request...")
    pk=pk.__str__()
    req = urllib.request.Request('http://models-api:8000/project2/api/v1/story/'+pk)

    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    resp = json.loads(resp_json)

    print(resp)
    return resp

@csrf_exempt
def add_story(story_dict):
    payload = story_dict
    response = requests.post('http://models-api:8000/project2/api/v1/story/create/', data=payload)
    json_data = response.json()
    json_data['type'] = "story"
    user_data = get_user(json_data['owner'])
    json_data['username'] = user_data['username']
    kafka_api.send_to_kafka(json_data)
    return response.json()

def get_music_videos(page):
    # make a GET request and parse the returned JSON
    # note, no timeouts, error handling or all the other things needed to do this for real
    print ("About to perform the GET request...")
    page=page.__str__()
    req = urllib.request.Request('http://models-api:8000/project2/api/v1/music_videos/?page='+page)

    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    resp = json.loads(resp_json)

    print(resp)
    return resp

def get_music_video(pk):
    # make a GET request and parse the returned JSON
    # note, no timeouts, error handling or all the other things needed to do this for real
    print ("About to perform the GET request...")
    pk=pk.__str__()
    req = urllib.request.Request('http://models-api:8000/project2/api/v1/music_videos/'+pk)

    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    resp = json.loads(resp_json)

    print(resp)
    return resp

@csrf_exempt
def add_music_video(music_vid_dict):
    payload = music_vid_dict
    response = requests.post('http://models-api:8000/project2/api/v1/music_videos/create/', data=payload)
    json_data = response.json()
    json_data['type'] = "music_video"
    user_data = get_user(json_data['owner'])
    json_data['username'] = user_data['username']
    kafka_api.send_to_kafka(json_data)
    return response.json()

def get_poems(page):
    # make a GET request and parse the returned JSON
    # note, no timeouts, error handling or all the other things needed to do this for real
    print ("About to perform the GET request...")
    page=page.__str__()
    req = urllib.request.Request('http://models-api:8000/project2/api/v1/poems/?page='+page)

    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    resp = json.loads(resp_json)

    print(resp)
    return resp

def get_poem(pk):
    # make a GET request and parse the returned JSON
    # note, no timeouts, error handling or all the other things needed to do this for real
    print ("About to perform the GET request...")
    pk=pk.__str__()
    req = urllib.request.Request('http://models-api:8000/project2/api/v1/poems/'+pk)

    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    resp = json.loads(resp_json)

    print(resp)
    return resp

@csrf_exempt
def add_poem(poem_dict):
    payload = poem_dict
    response = requests.post('http://models-api:8000/project2/api/v1/poems/create/', data=payload)
    json_data = response.json()
    json_data['type'] = "poem"
    user_data = get_user(json_data['owner'])
    json_data['username'] = user_data['username']
    kafka_api.send_to_kafka(json_data)
    return response.json()

def get_users(page):
    # make a GET request and parse the returned JSON
    # note, no timeouts, error handling or all the other things needed to do this for real
    print ("About to perform the GET request...")
    page=page.__str__()
    req = urllib.request.Request('http://models-api:8000/project2/api/v1/users/?page='+page)

    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    resp = json.loads(resp_json)

    print(resp)
    return resp

def get_user(pk):
    # make a GET request and parse the returned JSON
    # note, no timeouts, error handling or all the other things needed to do this for real
    print ("About to perform the GET request...")
    pk=pk.__str__()
    req = urllib.request.Request('http://models-api:8000/project2/api/v1/users/'+pk)

    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    resp = json.loads(resp_json)

    print(resp)
    return resp

@csrf_exempt
def get_user_by_username(username):
    payload = {'username':username}
    response = requests.get('http://models-api:8000/project2/api/v1/users/', params=payload)
    return response.json()

@csrf_exempt
def create_user(post_request):
    response = requests.post('http://models-api:8000/project2/api/v1/users/', data=post_request)
    return response.json()

@csrf_exempt
def create_auth(username):
    user = get_user_by_username(username)
    # whatisuser = str(user)
    id = user["results"][0]["id"]
    authenticator = uuid.uuid4()
    payload={"user_id":id, "authenticator":authenticator}
    # post_data = {'password': whatisuser, 'last_name': 'testing', 'username': 'blehh2222', 'first_name': 'password'}
    response = requests.post('http://models-api:8000/project2/api/v1/auth/', data=payload)
    # response = requests.post('http://models-api:8000/project2/api/v1/users/', data=post_data)
    return response.json()

@csrf_exempt
def get_auth(username):
    user = get_user_by_username(username)
    user_id = user["results"][0]["id"]
    response = requests.get('http://models-api:8000/project2/api/v1/auth/'+user_id)
    return response.json()

def get_stored_pw(username):
    user = get_user_by_username(username)
    user_pw = None
    if user["results"]:
        user_pw = user["results"][0]["password"]
    return user_pw

def verify_login(login_info):
    username = login_info["username"]
    password = login_info["password"]
    stored_pw = get_stored_pw(username)
    return hashers.check_password(password, stored_pw)

def delete_auth(auth):
    response = requests.delete('http://models-api:8000/project2/api/v1/auth/'+auth+'/delete')
    return response

def get_recommendations(item_id):
    item_type = ""
    if item_id.startswith("SONG"):
        item_type = "SONG"
    elif item_id.startswith("MUSIC_VID"):
        item_type = "MUSIC_VID"
    elif item_id.startswith("POEM"):
        item_type = "POEM"
    elif item_id.startswith("STORY"):
        item_type = "STORY"
    else:
        item_type = "IMAGE"

    response = requests.get('http://models-api:8000/project2/api/v1/recommendations/'+item_id)
    response = response.json() 
    recommendations = response["results"][0]["recommended_items"]
    # recommendations = recommendations.replace("[","")
    # recommendations = recommendations.replace("]","")
    # recommendations = recommendations.replace("'","")
    # recommendations.split(",")
    recommendations = ast.literal_eval(recommendations)

    same_type_recs = []

    for recommendation in recommendations:
        if recommendation.startswith(item_type):
            same_type_recs.append(int(recommendation[item_type.__len__():]))

    return same_type_recs