### Commands

- Install cassandra

- Connect to cassendra using shell
```
cqlsh --cqlversion="3.4.0"
```
or
```
cqlsh
```


- Making a keyspace
```
CREATE KEYSPACE movielens WITH replication = {'class': 'SimpleStrategy','replication_factor':'1'} AND durable_writes = true;
```
- Enter keyspace
```
USE movielens
```
- CRETAE TABLE
```
CREATE TABLE users (user_id int, age int, gender text, occupation text, zip text, PRIMARY KEY (user_id));
```
<i>Rremember: For cassandra the PRIMARY KEY is a must, because it is going to store all the other data wrt to the primary key's hash</i>

- Import data into the DB using spark
```
spark-submit --packages datastax:spark-cassandra-connector:2.0.0-M2-s_2.11 CassandraSpark.py
```

- Cleanup
```
sudo service cassandra stop
```