from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import render
import urllib.request, json
from django.http import HttpResponseNotFound
from urllib.request import urlopen
from django.http import JsonResponse
from django.http import Http404
from .forms import LoginForm, SignUpForm
from django.http import HttpResponseRedirect
import json
import requests
from django.middleware.csrf import get_token
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
    return render(request, 'index.html')

@csrf_exempt
def signup(request):
    if request.method == 'GET':
        form = SignUpForm()
        return render(request, 'signup.html', {'form': form})
    if request.method == 'POST':
        # csrf_token = get_token(request)
        # print ("About to perform the POST request...")
        post_data = {'first_name': 'lololololololol', 'last_name': 'testing', 'username': 'bbbbbbb', 'password': 'password'}
        # post_encoded = urllib.parse.urlencode(post_data).encode('utf-8')
        # req = urllib.request.Request('http://exp-api:8000/api/v1/users/', data=post_encoded, method='POST')
        response = requests.post('http://exp-api:8000/api/v1/users/',post_data,headers={'Content-Type': 'application/json'})
        return render(request, 'login.html')


def login(request):
    return render(request, 'login.html')

# def login(request):
#     # If we received a GET request instead of a POST request
#     if request.method == 'GET':
#         # display the login form page
#         return render(request, 'login.html')
#
#     if not f.is_valid():
#       # Form was bad -- send them back to login page and show them an error
#       return render('signup.html', ...)
#
#     # Creates a new instance of our login_form and gives it our POST data
#     f = login_form(request.POST)
#     return render(request, 'signup.html')

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LoginForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/login/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'login.html', {'form': form})


def search(request):
    req = urllib.request.Request('http://exp-api:8000/api/v1/songs/')
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    json_data = json.loads(resp_json)
    return render(request,
    'search.html',
    context={'data': json_data['results']})

def songs(request):
    """sending an exp service request to retrieve json data for songs"""
    req = urllib.request.Request('http://exp-api:8000/api/v1/songs/')
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    json_data = json.loads(resp_json)

    return render(
        request,
        'songs_homepage.html',
        context={'data': json_data['results']}
    )

def SongDetailView(request, id):
    """sending an exp service request to retrieve json data for a specific song"""
    try:
        req = urllib.request.Request('http://exp-api:8000/api/v1/songs/'+id)
        resp_json = urllib.request.urlopen(req).read().decode('utf-8')
        json_data = json.loads(resp_json)

        """this get's the owner's id and sends an exp service request to get their username back"""
        userid = str(json_data['owner'])
        userreq = urllib.request.Request('http://exp-api:8000/api/v1/users/'+userid)
        user_json = urllib.request.urlopen(userreq).read().decode('utf-8')
        user_data = json.loads(user_json)
    except:
        return HttpResponseNotFound('<h1>Page not found</h1>')

    return render(
        request,
        'song_detail.html',
        context={'data': json_data, 'username': user_data['username']}
    )

def music_videos(request):
    """sending an exp service request to retrieve json data for music videos"""
    req = urllib.request.Request('http://exp-api:8000/api/v1/music_videos/')
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    json_data = json.loads(resp_json)

    return render(
        request,
        'music_videos_homepage.html',
        context={'data': json_data['results']}
    )

def MusicVideoDetailView(request, id):
    """sending an exp service request to retrieve json data for a specific music video"""
    try:
        req = urllib.request.Request('http://exp-api:8000/api/v1/music_videos/'+id)
        resp_json = urllib.request.urlopen(req).read().decode('utf-8')
        json_data = json.loads(resp_json)

        """this get's the owner's id and sends an exp service request to get their username back"""
        userid = str(json_data['owner'])
        userreq = urllib.request.Request('http://exp-api:8000/api/v1/users/' + userid)
        user_json = urllib.request.urlopen(userreq).read().decode('utf-8')
        user_data = json.loads(user_json)
    except:
        return HttpResponseNotFound('<h1>Page not found</h1>')

    return render(
        request,
        'music_video_detail.html',
        context={'data': json_data, 'username': user_data['username']}
    )

def stories(request):
    """sending an exp service request to retrieve json data for stories"""
    req = urllib.request.Request('http://exp-api:8000/api/v1/stories/')
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    json_data = json.loads(resp_json)

    return render(
        request,
        'stories_homepage.html',
        context={'data': json_data['results']}
    )

def StoryDetailView(request, id):
    """sending an exp service request to retrieve json data for a specific story"""
    try:
        req = urllib.request.Request('http://exp-api:8000/api/v1/stories/'+id)
        resp_json = urllib.request.urlopen(req).read().decode('utf-8')
        json_data = json.loads(resp_json)

        """this get's the owner's id and sends an exp service request to get their username back"""
        userid = str(json_data['owner'])
        userreq = urllib.request.Request('http://exp-api:8000/api/v1/users/' + userid)
        user_json = urllib.request.urlopen(userreq).read().decode('utf-8')
        user_data = json.loads(user_json)
    except:
        return HttpResponseNotFound('<h1>Page not found</h1>')

    return render(
        request,
        'story_detail.html',
        context={'data': json_data, 'username': user_data['username']}
    )

def feedbacks(request):
    """sending an exp service request to retrieve json data for feedbacks"""
    req = urllib.request.Request('http://exp-api:8000/api/v1/feedbacks/')
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    json_data = json.loads(resp_json)

    return render(
        request,
        'feedbacks_homepage.html',
        context={'data': json_data['results']}
    )

def images(request):
    """sending an exp service request to retrieve json data for images"""
    req = urllib.request.Request('http://exp-api:8000/api/v1/images/')
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    json_data = json.loads(resp_json)

    return render(
        request,
        'images_homepage.html',
        context={'data': json_data['results']}
    )

def ImageDetailView(request, id):
    """sending an exp service request to retrieve json data for a specific image"""
    try:
        req = urllib.request.Request('http://exp-api:8000/api/v1/images/'+id)
        resp_json = urllib.request.urlopen(req).read().decode('utf-8')
        json_data = json.loads(resp_json)

        """this get's the owner's id and sends an exp service request to get their username back"""
        userid = str(json_data['owner'])
        userreq = urllib.request.Request('http://exp-api:8000/api/v1/users/' + userid)
        user_json = urllib.request.urlopen(userreq).read().decode('utf-8')
        user_data = json.loads(user_json)
    except:
        return HttpResponseNotFound('<h1>Page not found</h1>')
    return render(
        request,
        'image_detail.html',
        context={'data': json_data, 'username': user_data['username']}
    )


def poems(request):
    """sending an exp service request to retrieve json data for poems"""
    req = urllib.request.Request('http://exp-api:8000/api/v1/poems/')
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    json_data = json.loads(resp_json)

    return render(
        request,
        'poems_homepage.html',
        context={'data': json_data['results']}
    )

def PoemDetailView(request, id):
    """sending an exp service request to retrieve json data for a specific poem"""
    try:
        req = urllib.request.Request('http://exp-api:8000/api/v1/poems/'+id)
        resp_json = urllib.request.urlopen(req).read().decode('utf-8')
        json_data = json.loads(resp_json)

        """this get's the owner's id and sends an exp service request to get their username back"""
        userid = str(json_data['owner'])
        userreq = urllib.request.Request('http://exp-api:8000/api/v1/users/' + userid)
        user_json = urllib.request.urlopen(userreq).read().decode('utf-8')
        user_data = json.loads(user_json)
    except:
        return HttpResponseNotFound('<h1>Page not found</h1>')

    return render(
        request,
        'poem_detail.html',
        context={'data': json_data, 'username': user_data['username']}
    )


def handler404(request):
    return render(request, '404.html', status=404)

def handler400(request):
    return render(request, '400.html', status=400)

def handler500(request):
    return render(request, '500.html', status=500)
