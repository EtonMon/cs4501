from kafka import KafkaConsumer
import json
import time

# Attempting to establish with kafka every second for 20 seconds
timeout = 20
for i in range(timeout):
    time.sleep(1)
    try:
        print("----------------ATTEMPTING TO CONNECT TO SPARK-KAFKA----------------------", flush=True)
        consumer = KafkaConsumer('new-logs-topic', group_id='logs-indexer', bootstrap_servers=['kafka:9092'])
        print("----------------SUCCESSFULLY CONNECTED TO SPARK-KAFKA----------------------", flush=True)
        break
    except:
        print("----------------CONNECTION TO SPARK-KAFKA FAILED----------------------", flush=True)

# Attempts to process messages from kafka if connection established

try:
    print("----------------ATTEMPTING TO LISTEN FOR NEW LOGS----------------------", flush=True)
    #log_list=[]

    for message in consumer:
        print("log received",flush=True)
        new_log = json.loads((message.value).decode('utf-8'))
        writefile = open('access.log','a')
        #log_list.append(str(new_log['item_id'])+"\t"+str(new_log['user_id'])+"\n")
        writefile.write(str(new_log['item_id'])+"\t"+str(new_log['user_id'])+"\n")
        print(new_log,flush=True)
        writefile.close()
        #writefile.writelines(log_list)
except:
    print("----------------SPARK-KAFKA CONNECTION NEVER SUCCESSFULLY ESTABLISHED----------------------", flush=True)
