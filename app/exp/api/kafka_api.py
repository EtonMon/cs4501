from kafka import KafkaProducer
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def send_to_kafka(new_listing):
    producer = KafkaProducer(bootstrap_servers='kafka:9092')
    producer.send('new-listings-topic', json.dumps(new_listing).encode('utf-8'))
