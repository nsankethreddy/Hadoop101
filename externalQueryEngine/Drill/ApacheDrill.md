# Drill

Drill is just a system that sits on top of various technologie that help in storing data.

- It lets you execute SQL queries on data that might not even have a aschema at all and it certainly isnt relational.

- A SQL query engine for a variety of non relational databse and data files.

    - Have, MongoDB, HBase

    - Even flat JSON orParquet files on HDFS, S#, Azuew, Google cloud, local file system

- Based on Google's Dremel.

### Commands

Import data into Hive and MongoDB
- open hive view and create a database
    ```
        create database movielens;
    ```
- then upload u.data as ratings in movielens

- Use this command to find the scala and spark version you are using
    ```
        spark-submit --version
    ```

- add data into mongoDB
    ```
        spark-submit --packages org.mongodb.spark:mongo-spark-connector_2.11.8:2.3.0 MongoSpark.py 
    ```
- Installing drill
    
    Drill dosent come with the ambari sandbox (but we can install it using)
    ```
        wget http://archive.apache.org/dist/drill/drill-1.12.0/apache-drill-1.12.0.tar.gz

    ```
- And do some queries

    - select SQL in the options
        - to connect to mongo and execute queries

    ```
     select * from mongo.movielens.users LIMIT 10;
    ``` 

    - Join mongo and hive
    
    ```
     select u.occupation, count(*) from hive.movielens.ratings r JOIN mongo.movielens.users u ON r.user_id = u.user_id GROUP BY u.occupation 
    ```