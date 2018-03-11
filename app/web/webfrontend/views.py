from django.shortcuts import render
import urllib.request, json
from urllib.request import urlopen
from django.http import JsonResponse


# Create your views here.

def index(request):
    return render(request, 'index.html')

def songs(request):
    #retreiving data from url and converting to json format

    req = urllib.request.Request('http://exp-api:8000/api/v1/songs/')
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    json_data = json.loads(resp_json)

    #parsing json data

    for element in json_data['results']:
        artist = element['artists']
        owner = element['owner']
        title = element['title']
        time_posted = element['time_posted']
    return render(
        request,
        'songs_homepage.html',
        context={'data': json_data['results']}
    )

def music_videos(request):
    # retreiving data from url and converting to json format

    req = urllib.request.Request('http://exp-api:8000/api/v1/songs/')
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    json_data = json.loads(resp_json)

    return render(
        request,
        'music_videos_homepage.html',
        context={'data': json_data['results']}
    )

def stories(request):
    # retreiving data from url and converting to json format

    req = urllib.request.Request('http://exp-api:8000/api/v1/stories/')
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    json_data = json.loads(resp_json)

    return render(
        request,
        'stories_homepage.html',
        context={'data': json_data['results']}
    )

def feedbacks(request):
    # retreiving data from url and converting to json format

    req = urllib.request.Request('http://exp-api:8000/api/v1/feedbacks/')
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    json_data = json.loads(resp_json)

    return render(
        request,
        'feedbacks_homepage.html',
        context={'data': json_data['results']}
    )

def images(request):
    # retreiving data from url and converting to json format

    req = urllib.request.Request('http://exp-api:8000/api/v1/images/')
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    json_data = json.loads(resp_json)

    return render(
        request,
        'images_homepage.html',
        context={'data': json_data['results']}
    )

def poems(request):
    # retreiving data from url and converting to json format

    req = urllib.request.Request('http://exp-api:8000/api/v1/poems/')
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    json_data = json.loads(resp_json)

    return render(
        request,
        'poems_homepage.html',
        context={'data': json_data['results']}
    )
