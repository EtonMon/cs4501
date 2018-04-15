from kafka import KafkaConsumer
import json
import time

# Attempting to establish with kafka every second for 20 seconds
timeout = 20

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
                print(json.loads((message.value).decode('utf-8')))
except:
    print("----------------KAFA CONNECTION NEVER SUCCESSFULLY ESTABLISHED----------------------", flush=True)


# print("----------------ATTEMPTING TO CONNECT TO KAFKA----------------------")
# consumer = KafkaConsumer('new-listings-topic', group_id='listing-indexer', bootstrap_servers=['kafka:9092'])
# print("----------------BATCH SUCCESSFULLY CONNECTED TO KAFKA----------------------")
# retry = False

# print("----------------LISTENING FOR NEW LISTINGS----------------------")
# for message in consumer:
#             print(json.loads((message.value).decode('utf-8')))