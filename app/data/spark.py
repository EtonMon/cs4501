from pyspark import SparkContext

sc = SparkContext("spark://spark-master:7077", "PopularItems")

data = sc.textFile("/tmp/data/access.log", 2)     # each worker loads a piece of the data file

pairs = data.map(lambda line: line.split("\t"))   # tell each worker to split each line of it's partition

# userid, itemid
user_to_items = pairs.map(lambda pair: (pair[1], pair[0]))      # re-layout the data to ignore the user id
print(user_to_items.collect())

# userid, [itemid, itemid, itemid]
user_to_items_list = pairs.map(lambda pair: ((pair[1]),(pair[0]))).groupByKey()
# user_to_items_list = user_to_items.keys().groupByKey()
# print(user_to_items_list.map(lambda x : {x[0]: list(x[1])}).collect())

# userid, (itemid, itemid)
user_to_item_tuple = user_to_items_list.map(lambda user, itemlist: (user, (itemlist[0], itemlist[1])))

# (itemid, itemid), [userid, userid, userid] 
item_tuple_to_userlist = user_to_item_tuple.keys().groupByKey()

count = item_tuple_to_userlist.reduceByKey(lambda x,y: int(x)+len(y)) 
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

