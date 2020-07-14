# Spark 2

Extends RDD to a "Data Frame" object.  
  
DataFrame is DataSet of row objects.  

### DataFrames:
- Contain Row object(structured data)
- Can run SQL queries
- Has a schema (leading to more efficient storage)
- Read and write to JSON, Hive, Parquet
- Communicates with JDBC/ODBC, Tableau

### Using SparkSQL in python

- Imports
    - ``` from pyspark.sql import SQLContext, Row```
- Making a dataframe
    - ``` hivecontext = HiveContext(sc)```
    - ``` inputData = spark.read.json(datafile)```
- Create a database table
    - ``` inputData.createOrReplaceTempView("myStructuredStuff")```
- Run SQL queries
    - ``` myResultDataFrame = hiveContext.sql("""SELECT foo FROM bar ORDER BY foobar""")```

### Other stuff you can do with dataframes

- Coding more programitically rather than SQL
    - ``` myResultDataFrame.show()```
    - ``` myResultDataFrame.select("someFieldName")```
    - ``` myResultDataFrame.filter(myResultDataFrame("someFieldName" > 200)```
    - ``` myResultDataFrame.groupBy(myResultDataFrame("someFieldName")).mean()```

- Programming on lower (RDD) leave
    - ``` myResultDataFrame.rdd().map(mapperFunction)```


### SparkSQL Shell Access

- It can be used as a DB server just like Mysql and run SQL commands
- Start it with ``` sbin/start-thriftserver.sh```
- Listens to port 10000 by default.
- Connection using ``` bin/beeline -u jdbc:hive2://localhost:10000```

### UDFs
 User defined functions are suppored

 All the ML stuff are UDFs