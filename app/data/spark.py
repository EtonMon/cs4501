from pyspark import SparkContext
import mysql
import time


def extract_pair(line):
	pairlist = []
	iterablelist = list(line[1])
	for i in range(0, len(iterablelist)):
		for j in range(i+1, len(iterablelist)):
			pairlist.append((line[0], (iterablelist[i], iterablelist[j])))
	return (pairlist)

sc = SparkContext("spark://spark-master:7077", "PopularItems")

data = sc.textFile("/tmp/data/access.log", 2)     # each worker loads a piece of the data file

pairs = data.map(lambda line: line.split("\t"))   # tell each worker to split each line of it's partition

# userid, itemid
user_to_items = pairs.map(lambda pair: (pair[1], pair[0]))      # re-layout the data to ignore the user id
# print(user_to_items.collect())

# userid, [itemid, itemid, itemid]
user_to_items_list = pairs.map(lambda pair: ((pair[1]),(pair[0]))).groupByKey()
# user_to_items_list = user_to_items.keys().groupByKey()
# print(user_to_items_list.map(lambda x : {x[0]: list(x[1])}).collect())

# userid, (itemid, itemid)
user_to_item_tuple = user_to_items_list.flatMap(lambda line: extract_pair(line))
# print(user_to_item_tuple.collect())

# (itemid, itemid), [userid, userid, userid]
item_tuple_to_userlist = user_to_item_tuple.map(lambda pair: ((pair[1]),(pair[0]))).groupByKey()
# print(item_tuple_to_userlist.collect())
# print(item_tuple_to_userlist.map(lambda x : {x[0]: list(x[1])}).collect())
# item_tuple_to_userlist = user_to_item_tuple.keys().groupByKey()

count = item_tuple_to_userlist.reduceByKey(lambda x: len(x.values()))

# print(count.map(lambda x : {x[0]: len(x[1])}).collect())

use_count = count.map(lambda x : {x[0]: len(x[1])})

filtered_count = count.filter(lambda x: len(x[1]) > 1)

final_mappings = filtered_count.map(lambda x : x[0]).collect()

# print(final_mappings)
return_list = []
exists_list = []
for item in final_mappings:
    if item[0] not in exists_list:
        exists_list.append(item[0])
for idval in exists_list:
    appendlist = []
    for thing in final_mappings:
        if thing[0] == idval:
            appendlist.append(str(thing[1]))
    use_tuple = (idval, appendlist)
    return_list.append(use_tuple)

print(return_list)
starttime=time.time()
while True:
  
  mysql.update_db(return_list)
  time.sleep(120.0 - ((time.time() - starttime) % 120.0))

#print(count.collect())
sc.stop()
# print(count.collect())
# print(list((j[0], list(j[1])) for j in itemsGrouped.take(1)))
# sc.stop()
# count = items_mapped.reduceByKey(lambda x,y: int(x)+len(y))        # shuffle the data so that each key is only on one worker
                                                  # and then reduce all the values by adding them together
# output = count.collect()                          # bring the data back to the master node so we can print it out
# print("IN SPARK.PY")
# for page_id, count in output:
#     print ("page_id %s count %d" % (page_id, count))
# print ("Popular items done")
