# Functions to interact with elastic search
from elasticsearch import Elasticsearch

def query(query_string):
    """Json structure: {'empty':(is it empty), 'results':{'songs':...,'images':...,'stories':..., etc}}"""

    es = Elasticsearch(['es'])
    search_results = es.search(index='listing_index', body={'query': {'query_string': {'query': query_string}}, 'size': 100})
    #print(search_results)
    if search_results['timed_out'] is True or search_results['hits']['total'] is 0:
        return {'empty':True}
    else:
    
        hits = search_results['hits']['hits']

        response = {}
        response['empty'] = False
        results = {}
        songs = []
        images = []
        stories = []
        music_videos = []
        poems = []

        for listing in hits:
            print(listing['_source']['type'])
            if listing['_source']['type'] == 'song':
                id = listing['_source']['id']
                username = listing['_source']['username']
                owner = listing['_source']['owner']
                type = listing['_source']['type']
                title = listing['_source']['title']
                artists = listing['_source']['artists']
                
                songs.append({'id':id,'username':username,'owner':owner,'type':type,'title':title,'artists':artists})

            elif listing['_source']['type'] =='image':
                id = listing['_source']['id']
                username = listing['_source']['username']
                owner = listing['_source']['owner']
                type = listing['_source']['type']
                title = listing['_source']['title']
                artists = listing['_source']['artists']
                
                images.append({'id':id,'username':username,'owner':owner,'type':type,'title':title,'artists':artists})

            elif listing['_source']['type'] == 'story':
                id = listing['_source']['id']
                username = listing['_source']['username']
                owner = listing['_source']['owner']
                type = listing['_source']['type']
                title = listing['_source']['title']
                artists = listing['_source']['artists']
                text = listing['_source']['text']
                
                stories.append({'id':id,'username':username,'owner':owner,'type':type,'title':title,'artists':artists,'text':text})

            elif listing['_source']['type'] == 'music_video':
                id = listing['_source']['id']
                username = listing['_source']['username']
                owner = listing['_source']['owner']
                type = listing['_source']['type']
                title = listing['_source']['title']
                artists = listing['_source']['artists']
                
                music_videos.append({'id':id,'username':username,'owner':owner,'type':type,'title':title,'artists':artists})

            elif listing['_source']['type'] == 'poem':
                id = listing['_source']['id']
                username = listing['_source']['username']
                owner = listing['_source']['owner']
                type = listing['_source']['type']
                title = listing['_source']['title']
                artists = listing['_source']['artists']
                text = listing['_source']['text']
                
                poems.append({'id':id,'username':username,'owner':owner,'type':type,'title':title,'artists':artists,'text':text})

            results = {'songs':songs,'images':images,'stories':stories,'music_videos':music_videos,'poems':poems}

        response['results']=results

        return response

#print(query("etonmon"))