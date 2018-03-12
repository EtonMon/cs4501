from django.shortcuts import render
import urllib.request, json
from urllib.request import urlopen
from django.http import JsonResponse


# Create your views here.

def index(request):
    return render(request, 'index.html')

def signup(request):
    return render(request, 'signup.html')

def search(request):
    req = urllib.request.Request('http://exp-api:8000/api/v1/songs/')
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    json_data = json.loads(resp_json)
    return render(request,
    'search.html',
    context={'data': json_data['results']})

def songs(request):
    #retreiving data from url and converting to json format

    req = urllib.request.Request('http://exp-api:8000/api/v1/songs/')
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    json_data = json.loads(resp_json)

    return render(
        request,
        'songs_homepage.html',
        context={'data': json_data['results']}
    )

def SongDetailView(request, id):
    #retreiving data from url and converting to json format
    #getting information from a specific object

    req = urllib.request.Request('http://exp-api:8000/api/v1/songs/'+id)
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    json_data = json.loads(resp_json)

    # retreiving 'username' that is associated with the object from Custom_User json data

    userid = str(json_data['owner'])
    userreq = urllib.request.Request('http://exp-api:8000/api/v1/users/'+userid)
    user_json = urllib.request.urlopen(userreq).read().decode('utf-8')
    user_data = json.loads(user_json)

    return render(
        request,
        'song_detail.html',
        context={'data': json_data, 'username': user_data['username']}
    )

def music_videos(request):
    # retreiving data from url and converting to json format

    req = urllib.request.Request('http://exp-api:8000/api/v1/music_videos/')
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    json_data = json.loads(resp_json)

    return render(
        request,
        'music_videos_homepage.html',
        context={'data': json_data['results']}
    )

def MusicVideoDetailView(request, id):
    #retreiving data from url and converting to json format
    #getting information from a specific object

    req = urllib.request.Request('http://exp-api:8000/api/v1/music_videos/'+id)
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    json_data = json.loads(resp_json)

    # retreiving 'username' that is associated with the object from Custom_User json data

    userid = str(json_data['owner'])
    userreq = urllib.request.Request('http://exp-api:8000/api/v1/users/' + userid)
    user_json = urllib.request.urlopen(userreq).read().decode('utf-8')
    user_data = json.loads(user_json)

    return render(
        request,
        'music_video_detail.html',
        context={'data': json_data, 'username': user_data['username']}
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

def StoryDetailView(request, id):
    #retreiving data from url and converting to json format
    #getting information from a specific object

    req = urllib.request.Request('http://exp-api:8000/api/v1/stories/'+id)
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    json_data = json.loads(resp_json)

    # retreiving 'username' that is associated with the object from Custom_User json data

    userid = str(json_data['owner'])
    userreq = urllib.request.Request('http://exp-api:8000/api/v1/users/' + userid)
    user_json = urllib.request.urlopen(userreq).read().decode('utf-8')
    user_data = json.loads(user_json)

    return render(
        request,
        'story_detail.html',
        context={'data': json_data, 'username': user_data['username']}
    )

def feedbacks(request):
    # retreiving data from url and converting to json format
    # getting information from a specific object

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

def ImageDetailView(request, id):
    #retreiving data from url and converting to json format
    #getting information from a specific object

    req = urllib.request.Request('http://exp-api:8000/api/v1/images/'+id)
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    json_data = json.loads(resp_json)

    # retreiving 'username' that is associated with the object from Custom_User json data

    userid = str(json_data['owner'])
    userreq = urllib.request.Request('http://exp-api:8000/api/v1/users/' + userid)
    user_json = urllib.request.urlopen(userreq).read().decode('utf-8')
    user_data = json.loads(user_json)

    return render(
        request,
        'image_detail.html',
        context={'data': json_data, 'username': user_data['username']}
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

def PoemDetailView(request, id):
    #retreiving data from url and converting to json format
    #getting information from a specific object

    req = urllib.request.Request('http://exp-api:8000/api/v1/poems/'+id)
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    json_data = json.loads(resp_json)

    # retreiving 'username' that is associated with the object from Custom_User json data

    userid = str(json_data['owner'])
    userreq = urllib.request.Request('http://exp-api:8000/api/v1/users/' + userid)
    user_json = urllib.request.urlopen(userreq).read().decode('utf-8')
    user_data = json.loads(user_json)

    return render(
        request,
        'poem_detail.html',
        context={'data': json_data, 'username': user_data['username']}
    )
