import urllib.request
import urllib.parse
import json
import os
import hmac
import requests
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import hashers

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
    authenticator = hmac.new(
        key = settings.SECRET_KEY.encode('utf-8'),
        msg = os.urandom(32),
        digestmod = 'sha256',
    ).hexdigest()
    payload={"user_id":id, "authenticator":authenticator}
    # post_data = {'password': whatisuser, 'last_name': 'testing', 'username': 'blehh2222', 'first_name': 'password'}
    response = requests.post('http://models-api:8000/project2/api/v1/auth/', data=payload)
    # response = requests.post('http://models-api:8000/project2/api/v1/users/', data=post_data)
    return response.json()

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
