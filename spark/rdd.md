# RDD
Resilient Distributed Dataset

### Creating RDDs:

- Directly
```
nums = sc.parallize([1,2,3,4])
```
- Converting a text file into  RDD
```
sc.textFile("file://<location of file in localsystem/hdfs cluster/>") 
```
or
```
sc.textFile("s3n://<url for the file adress in AWS>)
```
- From Hive
```
hiveCtx = HiveContext(sc)
```
And Execute SQL queries of Hive Context from within spark.  
Eg:
```
rows = hiveCtx.sql("SELECT name, age FORM students)
```
- From any DB  

Eg: JDBC, Cassandra, HBase, ... etc.

### Mapping in RDD:
- Example:
```
nums = sc.parallize([1,2,3,4])
squaredRDD= rdd.map(lambda x:x*x)
```
### Reducing in RDD:
- collect
- count
- countByValue
- take
- top
- reduce
- ... and more ..

