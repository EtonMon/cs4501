from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import render
import urllib.request, json
from django.http import HttpResponseNotFound
from urllib.request import urlopen
from django.http import JsonResponse
from django.http import Http404
from .forms import LoginForm, SignUpForm, StoryForm, MusicVideoForm
from .forms import SongForm, PoemForm, ImageForm
from django.http import HttpResponseRedirect
import json
import requests
from django.middleware.csrf import get_token
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.urls import reverse
from django.contrib import messages


# Create your views here.

def index(request):
    username = request.COOKIES.get('username')
    return render(request, 'index.html', context={'username': username})

@csrf_exempt
def signup(request):
    if request.method == 'GET':
        form = SignUpForm()
        return render(request, 'signup.html', {'form': form})
    if request.method == 'POST':
        response = requests.post('http://exp-api:8000/api/v1/users/',data=json.dumps(request.POST),headers={'Content-Type': 'application/json'})
        try:
            if response.json()["user_in_db"]:
                messages.error(request, "That username already exists.")
                form = SignUpForm()
                return render(request, 'signup.html', {'form': form})
        except:
            return HttpResponseRedirect('/login/')

@csrf_exempt
def login(request):
    if 'auth' in request.COOKIES:
        return HttpResponseRedirect('/home/')
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if not form.is_valid():
            #messages.error(request, "Please enter a valid username")
            return render(request, 'index.html', {'form': form})
        payload = json.dumps(request.POST)
        response = requests.post('http://exp-api:8000/api/v1/login/', data=request.POST.dict())
        response_str = response.content.decode('utf-8')
        response_json = json.loads(response_str)
        try:
            authenticator = response_json['authenticator']
            user_id = str(response_json['user_id'])
            response = HttpResponseRedirect('/home/')
            response.set_cookie("auth", authenticator)
            response.set_cookie("id", user_id)
            response.set_cookie("username", form.cleaned_data['username'])
            #logged_in = 'True'
            return response
        except:
            #logged_in = 'False'
            messages.error(request, "Either username or password was invalid. Please try again.")
            return render(request, 'login.html', {'form': form})

@csrf_exempt
def logout(request):
    requests.post('http://exp-api:8000/api/v1/logout/', data={"auth": request.COOKIES.get('auth'), "user_id": request.COOKIES.get('user_id')})
    response = HttpResponseRedirect('/home/')
    response.delete_cookie('auth')
    response.delete_cookie('id')
    response.delete_cookie('username')
    return response

@csrf_exempt
def search(request):
    if request.method == 'POST':
        response = requests.post('http://exp-api:8000/api/v1/search/', data=request.POST.dict())
        formsubmission = request.POST.dict()
        response_str = response.content.decode('utf-8')
        response_json = json.loads(response_str)
        if response_json['empty']==True:
            return render(request,
            'search.html', context={'query': formsubmission['query']})
        return render(request,
        'search.html',
        context={'data': response_json['results'], 'query': formsubmission['query']})
    else:
        return HttpResponseNotFound('<h1>Page isnt found</h1>')

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
        auth = request.COOKIES.get('auth')
        auth_bool = True
        if not auth:
            auth_bool = False

        req = urllib.request.Request('http://exp-api:8000/api/v1/songs/'+id+"?auth="+str(auth_bool)+"&user_id="+str(request.COOKIES.get('id')))
        resp_json = urllib.request.urlopen(req).read().decode('utf-8')
        json_data = json.loads(resp_json)

        """this get's the owner's id and sends an exp service request to get their username back"""
        userid = str(json_data['owner'])
        userreq = urllib.request.Request('http://exp-api:8000/api/v1/users/'+userid)
        user_json = urllib.request.urlopen(userreq).read().decode('utf-8')
        user_data = json.loads(user_json)

        recommendedreq = urllib.request.Request('http://exp-api:8000/api/v1/songs/recommendations/' + id)
        recommended_json = urllib.request.urlopen(recommendedreq).read().decode('utf-8')
        recommended_data = json.loads(recommended_json)
        id_list = recommended_data['recommendations']

        itemslist = []

        for itemid in id_list:
            itemreq = urllib.request.Request('http://exp-api:8000/api/v1/songs/'+str(itemid)+"?auth="+str(auth_bool)+"&user_id="+str(request.COOKIES.get('id')))
            item_decoded = urllib.request.urlopen(itemreq).read().decode('utf-8')
            item_data = json.loads(item_decoded)
            itemslist.append(item_data)
    except:
        return HttpResponseNotFound('<h1>Page not found</h1>')

    return render(
        request,
        'song_detail.html',
        context={'data': json_data, 'username': user_data['username'], 'recommendations': itemslist}
    )

def music_videos(request):
    """sending an exp service request to retrieve json data for music videos"""
    req = urllib.request.Request('http://exp-api:8000/api/v1/music_videos/')
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    json_data = json.loads(resp_json)
    userreq = urllib.request.Request('http://exp-api:8000/api/v1/users/')
    user_json = urllib.request.urlopen(userreq).read().decode('utf-8')
    user_data = json.loads(user_json)

    # return HttpResponse(json_data['results'])
    return render(
        request,
        'music_videos_homepage.html',
        context={'data': json_data['results'], 'user_data': user_data['results']}
    )

def MusicVideoDetailView(request, id):
    """sending an exp service request to retrieve json data for a specific music video"""
    try:
        auth = request.COOKIES.get('auth')
        auth_bool = True
        if not auth:
            auth_bool = False

        req = urllib.request.Request('http://exp-api:8000/api/v1/music_videos/'+id+"?auth="+str(auth_bool)+"&user_id="+str(request.COOKIES.get('id')))
        resp_json = urllib.request.urlopen(req).read().decode('utf-8')
        json_data = json.loads(resp_json)

        """this get's the owner's id and sends an exp service request to get their username back"""
        userid = str(json_data['owner'])
        userreq = urllib.request.Request('http://exp-api:8000/api/v1/users/' + userid)
        user_json = urllib.request.urlopen(userreq).read().decode('utf-8')
        user_data = json.loads(user_json)

        """send request for recommendations list for single item"""
        recommendedreq = urllib.request.Request('http://exp-api:8000/api/v1/music_videos/recommendations/' + id)
        recommended_json = urllib.request.urlopen(recommendedreq).read().decode('utf-8')
        recommended_data = json.loads(recommended_json)
        music_videos_list = recommended_data['recommendations']

        music_videos = []

        for musicvideoid in music_videos_list:
            musicvideoreq = urllib.request.Request('http://exp-api:8000/api/v1/music_videos/'+str(musicvideoid)+"?auth="+str(auth_bool)+"&user_id="+str(request.COOKIES.get('id')))
            musicvideo_decoded = urllib.request.urlopen(musicvideoreq).read().decode('utf-8')
            musicvideo_data = json.loads(musicvideo_decoded)
            music_videos.append(musicvideo_data)
    except:
        return HttpResponseNotFound('<h1>Page not found</h1>')

    return render(
        request,
        'music_video_detail.html',
        context={'data': json_data, 'username': user_data['username'],'recommendations':music_videos}
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
        auth = request.COOKIES.get('auth')
        auth_bool = True
        if not auth:
            auth_bool = False

        req = urllib.request.Request('http://exp-api:8000/api/v1/stories/'+id+"?auth="+str(auth_bool)+"&user_id="+str(request.COOKIES.get('id')))
        resp_json = urllib.request.urlopen(req).read().decode('utf-8')
        json_data = json.loads(resp_json)

        """this get's the owner's id and sends an exp service request to get their username back"""
        userid = str(json_data['owner'])
        userreq = urllib.request.Request('http://exp-api:8000/api/v1/users/' + userid)
        user_json = urllib.request.urlopen(userreq).read().decode('utf-8')
        user_data = json.loads(user_json)

        recommendedreq = urllib.request.Request('http://exp-api:8000/api/v1/stories/recommendations/' + id)
        recommended_json = urllib.request.urlopen(recommendedreq).read().decode('utf-8')
        recommended_data = json.loads(recommended_json)
        id_list = recommended_data['recommendations']

        itemslist = []

        for itemid in id_list:
            itemreq = urllib.request.Request('http://exp-api:8000/api/v1/stories/'+str(itemid)+"?auth="+str(auth_bool)+"&user_id="+str(request.COOKIES.get('id')))
            item_decoded = urllib.request.urlopen(itemreq).read().decode('utf-8')
            item_data = json.loads(item_decoded)
            itemslist.append(item_data)

    except:
        return HttpResponseNotFound('<h1>Page not found</h1>')

    return render(
        request,
        'story_detail.html',
        context={'data': json_data, 'username': user_data['username'], 'recommendations': itemslist}
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
        auth = request.COOKIES.get('auth')
        auth_bool = True
        if not auth:
            auth_bool = False

        req = urllib.request.Request('http://exp-api:8000/api/v1/images/'+id+"?auth="+str(auth_bool)+"&user_id="+str(request.COOKIES.get('id')))
        resp_json = urllib.request.urlopen(req).read().decode('utf-8')
        json_data = json.loads(resp_json)

        """this get's the owner's id and sends an exp service request to get their username back"""
        userid = str(json_data['owner'])
        userreq = urllib.request.Request('http://exp-api:8000/api/v1/users/' + userid)
        user_json = urllib.request.urlopen(userreq).read().decode('utf-8')
        user_data = json.loads(user_json)

        recommendedreq = urllib.request.Request('http://exp-api:8000/api/v1/images/recommendations/' + id)
        recommended_json = urllib.request.urlopen(recommendedreq).read().decode('utf-8')
        recommended_data = json.loads(recommended_json)
        id_list = recommended_data['recommendations']

        itemslist = []

        for itemid in id_list:
            itemreq = urllib.request.Request('http://exp-api:8000/api/v1/images/'+str(itemid)+"?auth="+str(auth_bool)+"&user_id="+str(request.COOKIES.get('id')))
            item_decoded = urllib.request.urlopen(itemreq).read().decode('utf-8')
            item_data = json.loads(item_decoded)
            itemslist.append(item_data)
    except:
        return HttpResponseNotFound('<h1>Page not found</h1>')
    return render(
        request,
        'image_detail.html',
        context={'data': json_data, 'username': user_data['username'], 'recommendations': itemslist}
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
        auth = request.COOKIES.get('auth')
        auth_bool = True
        if not auth:
            auth_bool = False

        req = urllib.request.Request('http://exp-api:8000/api/v1/poems/'+id+"?auth="+str(auth_bool)+"&user_id="+str(request.COOKIES.get('id')))
        resp_json = urllib.request.urlopen(req).read().decode('utf-8')
        json_data = json.loads(resp_json)

        """this get's the owner's id and sends an exp service request to get their username back"""
        userid = str(json_data['owner'])
        userreq = urllib.request.Request('http://exp-api:8000/api/v1/users/' + userid)
        user_json = urllib.request.urlopen(userreq).read().decode('utf-8')
        user_data = json.loads(user_json)

        recommendedreq = urllib.request.Request('http://exp-api:8000/api/v1/poems/recommendations/' + id)
        recommended_json = urllib.request.urlopen(recommendedreq).read().decode('utf-8')
        recommended_data = json.loads(recommended_json)
        id_list = recommended_data['recommendations']

        itemslist = []

        for itemid in id_list:
            itemreq = urllib.request.Request('http://exp-api:8000/api/v1/poems/'+str(itemid)+"?auth="+str(auth_bool)+"&user_id="+str(request.COOKIES.get('id')))
            item_decoded = urllib.request.urlopen(itemreq).read().decode('utf-8')
            item_data = json.loads(item_decoded)
            itemslist.append(item_data)

    except:
        return HttpResponseNotFound('<h1>Page not found</h1>')

    return render(
        request,
        'poem_detail.html',
        context={'data': json_data, 'username': user_data['username'], 'recommendations': itemslist}
    )

@csrf_exempt
def create_story(request):
    auth = request.COOKIES.get('auth')
    if not auth:
        return HttpResponseRedirect('/home/')
    if request.method == 'GET':
        form = StoryForm()
        return render(request, 'create_story.html', {'form': form})
    if request.method == 'POST':
        owner = int(request.COOKIES.get('id'))
        title = request.POST['title']
        artists = request.POST['artists']
        text = request.POST['text']
        json_post = {"title": title, "artists": artists, "owner": owner, "text": text}
        response = requests.post('http://exp-api:8000/api/v1/stories/',data=json.dumps(json_post),headers={'Content-Type': 'application/json'})
        return HttpResponseRedirect('/stories/')

@csrf_exempt
def create_music_video(request):
    auth = request.COOKIES.get('auth')
    if not auth:
        return HttpResponseRedirect('/home/')
    if request.method == 'GET':
        form = MusicVideoForm()
        return render(request, 'create_music_video.html', {'form': form})
    if request.method == 'POST':
        owner = int(request.COOKIES.get('id'))
        title = request.POST['title']
        artists = request.POST['artists']
        json_post = {"title": title, "artists": artists, "owner": owner}
        response = requests.post('http://exp-api:8000/api/v1/music_videos/',data=json.dumps(json_post),headers={'Content-Type': 'application/json'})
        return HttpResponseRedirect('/music_videos/')

@csrf_exempt
def create_poem(request):
    auth = request.COOKIES.get('auth')
    if not auth:
        return HttpResponseRedirect('/home/')
    if request.method == 'GET':
        form = PoemForm()
        return render(request, 'create_poem.html', {'form': form})
    if request.method == 'POST':
        owner = int(request.COOKIES.get('id'))
        title = request.POST['title']
        artists = request.POST['artists']
        text = request.POST['text']
        json_post = {"title": title, "artists": artists, "owner": owner, "text": text}
        response = requests.post('http://exp-api:8000/api/v1/poems/',data=json.dumps(json_post),headers={'Content-Type': 'application/json'})
        return HttpResponseRedirect('/poems/')

@csrf_exempt
def create_image(request):
    auth = request.COOKIES.get('auth')
    if not auth:
        return HttpResponseRedirect('/home/')
    if request.method == 'GET':
        form = ImageForm()
        return render(request, 'create_image.html', {'form': form})
    if request.method == 'POST':
        owner = int(request.COOKIES.get('id'))
        title = request.POST['title']
        artists = request.POST['artists']
        json_post = {"title": title, "artists": artists, "owner": owner}
        response = requests.post('http://exp-api:8000/api/v1/images/',data=json.dumps(json_post),headers={'Content-Type': 'application/json'})
        return HttpResponseRedirect('/images/')

@csrf_exempt
def create_song(request):
    auth = request.COOKIES.get('auth')
    if not auth:
        return HttpResponseRedirect('/home/')
    if request.method == 'GET':
        form = SongForm()
        return render(request, 'create_song.html', {'form': form})
    if request.method == 'POST':
        owner = int(request.COOKIES.get('id'))
        title = request.POST['title']
        artists = request.POST['artists']
        json_post = {"title": title, "artists": artists, "owner": owner}
        response = requests.post('http://exp-api:8000/api/v1/songs/',data=json.dumps(json_post),headers={'Content-Type': 'application/json'})
        return HttpResponseRedirect('/songs/')

"""
def SearchDetailView(request, id):
    sending an exp service request to retrieve json data for a specific poem
    try:
        req = urllib.request.Request('http://exp-api:8000/api/v1/search/'+id)
        resp_json = urllib.request.urlopen(req).read().decode('utf-8')
        json_data = json.loads(resp_json)

        this get's the owner's id and sends an exp service request to get their username back
        userid = str(json_data['owner'])
        userreq = urllib.request.Request('http://exp-api:8000/api/v1/users/' + userid)
        user_json = urllib.request.urlopen(userreq).read().decode('utf-8')
        user_data = json.loads(user_json)
    except:
        return HttpResponseNotFound('<h1>Page not found</h1>')

    return render(
        request,
        'search.html',
        context={'data': json_data, 'username': user_data['username']}
    )
"""
def handler404(request):
    return render(request, '404.html', status=404)

def handler400(request):
    return render(request, '400.html', status=400)

def handler500(request):
    return render(request, '500.html', status=500)
