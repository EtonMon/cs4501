import urllib.request
import urllib.parse
import json

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
