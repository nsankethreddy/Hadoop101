# MongoDB

Favours Consistency over availability.   
(ie it has a primary node ,if the primary node dies we could still read from the database but we cannot write until the issue is resolved).

### Features:

- No real schema is enforced on the data.
    (It does this by appending a unique ID to every blog of data that is added to the DB)
    - Although, you can insert a schema if you want to.

- Terminology
    - Databases
    - Collections
    - Documents

- Shell is a full JavaScript interpreter

- It alone can act as replcement for Hadoop
    - It has aggregation capabilities
    - It can exectue Map-reduce codes directly
    - And it has its own File system called GridFS

- But it still integrates with Hadoop, Spark and most languages.

### Commands:

- To import the data into the mongoDB using spark from HDFS

```
spark-submit --packages org.mogobd.spark:mongo-spark-cpnnector_2.11:2.4.2 MongoSpark.py
```

- To access the mongo shell
```
mongo
```
- Some Mongo shell commands:
    - ```
        use movielens
      ```
    - ```
        db.users.find( {user_id:100} )
      ```
    - ```
        db.users.explain().find( {user_id:100} )
      ```
        <i> .```explain``` command tells us what happens under the hood </i>
    - ```
        db.users.aggregate([{ $group: { _id: {occupation: "occupation"}, avgAge: {$avg: "$avg"}}}])
      ```
    - ```
        db.users.count()
      ```
    - ```
        db.getCollectionInfos()
      ```
    - ```
        db.users.drop()
      ```