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
    print("----------------KAFA CONNECTION NEVER SUCCESSFULLY ESTABLISHED----------------------", flush=True)
