from kafka import KafkaConsumer
from elasticsearch import Elasticsearch
import json
import time

# Attempting to establish with kafka every second for 20 seconds
timeout = 20
es = Elasticsearch(['es'])
for i in range(timeout):
    time.sleep(1)
    try:
        print("----------------ATTEMPTING TO CONNECT TO KAFKA----------------------", flush=True)
        consumer = KafkaConsumer('new-listings-topic', group_id='listing-indexer', bootstrap_servers=['kafka:9092'])
        print("----------------SUCCESSFULLY CONNECTED TO KAFKA----------------------", flush=True)
        break
    except:
        print("----------------CONNECTION TO KAFKA FAILED----------------------", flush=True)

# Create ES index by adding and deleting trivial listing
for i in range(timeout):
    time.sleep(1)
    try:
        print("----------------ATTEMPTING TO CREATE ES INDEX----------------------", flush=True)
        some_new_listing = {'title': 'Used MacbookAir 13"', 'description': 'This is a used Macbook Air in great condition', 'id':42, 'type':'None'}
        es.index(index='listing_index', doc_type='listing', id=some_new_listing['id'], body=some_new_listing)
        es.indices.refresh(index="listing_index")
        es.delete(index='listing_index', doc_type='listing', id=some_new_listing['id'])
        es.indices.refresh(index="listing_index")
        print("----------------INDEX CREATION SUCCESSFUL----------------------", flush=True)
        break
    except:
        print("----------------INDEX CREATION FAILED----------------------", flush=True)


# Attempts to process messages from kafka if connection established
try:
    print("----------------ATTEMPTING TO LISTEN FOR NEW LISTINGS----------------------", flush=True)
    for message in consumer:
        print("item received",flush=True)
        new_listing = json.loads((message.value).decode('utf-8'))
        print(new_listing,flush=True)
        es.index(index='listing_index', doc_type='listing', id=new_listing['id'], body=new_listing)
        es.indices.refresh(index="listing_index")
except:
    print("----------------KAFKA CONNECTION NEVER SUCCESSFULLY ESTABLISHED----------------------", flush=True)
