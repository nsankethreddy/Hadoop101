# Hive
![Hive image](../media/hive.png)

Hive is a architecture that lets you run sequel queries accross entire Cluster. It works by translating your SQL into map-reduce or tez commands.

### Advantages of hive:
- Familier SQL syntaxes
- Interactive
- Scalable (Most appropriate for Big data)
- UDFs

### Disadvantages of hive:
- High latency(cannot be used for online transactions in realtime)
- Stores data in a denormalised fasion(Does not have foreign keys concept)
- SQL has its limits (More complex queries can be done with Pig or spark)
- No record-level updates, inserts and deletes.

The variation of SQL used in hive is the HiveQL, it is pretty much the same thing as MySql with some extensions ( Eg: "view"..can store the results of a query in a "view", which subsequent queries can use as a table )


Eg: Top rated movies
```
CREATE view IF NOT EXISTS topMovieIDs AS
SELECT movieID, count(movieID) as ratingCount
FROM ratings
GROUP BY movieID
ORDER BY ratingCount DESC;

SELECT n.title ratingCount
FROM topMovieIDs t JOIN names n ON t.movieID = n.movieID;
```
```
DROP view topMovieIDs
```

## More about Hive
One of the basic concepts of hive is SCHEMA ON READ, this is what seperates it from the other traditional DBs.

Hive maintains a "metastore" tha imparts a structure you define on the unstructured data that is stored on HDFS etc.

For uploading the existing data in to the Hive Db
```
CREATE TABLE ratings(
    userID INT,
    movieID INT,
    rating INT,
    time INT)
)
ROW FORMAT DELIMTED FIELDS TERMININATED BY '\t'
STORED AS TEXTFILE;

LOAD DATA LOCAL INPATH '$(env:HOME)/ml-100k/u.data'
OVERWRITE INTO TABLE ratings;
```

### Where is the data?
- ``` LOAD DATA```
    - Moves data from a distributed filesystem into Hive
    - Hive Ownes that data (ie. if you drop a table it completely drops it)
- ```LOAD DATA LOCAL```
    - COPIES data from local filesystem into Hive
    - Hive Ownes that data (ie. if you drop a table it completely drops it)
- Managed vs. External tables
    - Makes a copy of the data in the Hive file system and loses ownership(ie. if you drop the table the system only deletes the matadata and leaves the data as it is)
    ```
    CREATE EXTERNAL TABLE IF NOT EXISTS ratings(
        userID INT,
        movieID INT,
        rating INT,
        time INT)
    ROW FORMAT DELIMTED FIELDS TERMININATED BY '\t'
    LOCATION '/data/ml-100k/u.data';
    ```
### Partitioning 

Its used for optimization (IF the query is related to only a part of data, we could partition the DB and then run queries on it)

```
CREATE TABLE customers(
    name STRING,
    address STRUCT<street:STRING, city:string,state:STRING, zip:INT>
)
PARTITIONED BY (country STRING);
```
This is going to result in the customers table to be broken like
```
.../customers/country=CA/..
.../customers/country=CB/...
...
```

### Ways to use hive
- Interactive CLI by typing ```hive``` in the terminal
- Run Saved query files like
  ``` hive -f /path/queries.hql ```
- Through ambari
- JDBC/ODBC
- Via Oozi