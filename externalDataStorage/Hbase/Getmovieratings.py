"""
For running this HBASE code we need to setup a open port for HBaseREST on 127.0.0.1:8000 and 8000 and then run the REST api in the ambari using the command 
"/usr/hdp/current/hbase-master/bin/hbase-daemon.sh start rest -p 8000 --infoport 8001"

Abd after executing the code clean up using 
"/usr/hdp/current/hbase-master/bin/hbase-daemon.sh stop rest"
"""
from starbase import Connection

c = Connection("127.0.0.1", "8000")

ratings = c.table('ratings')

if(ratings.exists()):
    print("Dropping existing ratings table\n")
    ratings.drop()

ratings.create('rating')

print("Parsing the ml-100k ratings data..")

ratingFile = open("../../ml-100k/u.data","r")

batch = ratings.batch()

for line in ratingFile:
    (userID, movieID, rating, timestamp) = line.split()
    batch.update(userID, {'rating':{movieID: rating}})

ratingFile.close()

print ("committing ratings data to HBase via REST service\n")
batch.commit(finalize=True)

print ("Get back ratings for users... \n")
print ("Ratings for user ID 1\n")
print (ratings.fetch("1"))
print ("Ratings for user ID 33\n")
print (ratings.fetch("33"))
