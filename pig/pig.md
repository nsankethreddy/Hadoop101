# PIG

Pig is above Map-reduce and tez which are above YARN which is above HDFS.

Pig introduces PigLatin, a scripting language that lets you use SQL-Like syntax to define your map and reduce steps. 

Pig works better with tez and is much faster that map-reduce in terms of performance. 

Supports UDFs(User Defined functions)

Running Pig:
- Grunt
- Script
- Ambari/Hue

## Commands:
Returns tupule of information[LOAD,AS]    
```
ratings = LOAD '/user/maria_dev/ml-100k/u.data' AS (userID:int, movieID:int, rating:int, ratingTime:int);
```
If the seperator is not \t (here it is a '|' symbol)[USING PigStorage]
```
metadata = LOAD '/user/maria_dev/ml-100k/u.item' USING PigStorage('|') AS (movieID:int, movieTitle:chararray, releaseDate:chararray, videoRealese:chararray, imdblink:chararray);
```
To fix the date-time [FOREACH,GENERATE]
```
nameLookup = FOREACH metadata GENERATE movieID, movieTitle, ToUnixTime(ToDate(releaseDate, 'dd-MMM-yyyy')) AS releaseTime;
```
[GROUP,BY,DUMP]
It creates and returns a bag(a tupule of all the values that satisfy)
```
ratingsByMovie = GROUP ratings BY movieID;

DUMP ratingsByMovie;
```
[AVG]
```
avgRatings = FOREACH ratingsByMovie GENERATE group as movieID, AVG(ratings.rating) as avgRating;

DUMP avgRatings;
```
[DESCRIBE]
Gives table info
```
DESCRIBE ratings
```
[FILTER]
```
goodmovies = FILTER avgRatings BY avgRating > 4.0;
```
[JOIN,BY]
```
goodmoviesWithData = JOIN goodmovies BY movieID, nameLookup BY movieID;
```
[ORDER]
```
orderGoodmovies = ORDER goodmoviesWithData BY nameLookup::releaseTime;

DUMP orderGoodmovies;
```

## Everything put together:
- script1
```
ratings = LOAD '/user/maria_dev/ml-100k/u.data' AS (userID:int, movieID:int, rating:int, ratingTime:int);
metadata = LOAD '/user/maria_dev/ml-100k/u.item' USING PigStorage('|')
	AS (movieID:int, movieTitle:chararray, releaseDate:chararray, videoRealese:chararray, imdblink:chararray);
   
nameLookup = FOREACH metadata GENERATE movieID, movieTitle,
	ToUnixTime(ToDate(releaseDate, 'dd-MMM-yyyy')) AS releaseTime;
   
ratingsByMovie = GROUP ratings BY movieID;
avgRatings = FOREACH ratingsByMovie GENERATE group as movieID, AVG(ratings.rating) as avgRating;
goodmovies = FILTER avgRatings BY avgRating > 4.0;
goodmoviesWithData = JOIN goodmovies BY movieID, nameLookup BY movieID;
ordergoodMovies = ORDER goodmoviesWithData BY nameLookup::releaseTime;
DUMP ordergoodMovies;
```

## Extra pig commands:

- STORE (opposite of load)
```
STORE result INTO 'result1' USING PigStorage(':'); 
```
- DISTINCT, MAPREDUCE, STREAM, SAMPLE
- COGROUP(JOIN), GROUP, CROSS, CUBE
- RANK, LIMIT
- UNION, SPLIT
- AVG, CONCAT, COUNT, MAX, MIN, SIZE, SUM
- DESCRIBE, EXPLAIN, ILLUSTRATE

## UDFs
Written in java
- REGISTER
- DEFINE
- IMPORT
