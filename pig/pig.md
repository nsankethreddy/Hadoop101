# PIG

Pig is above Map-reduce and tez which are above YARN which is above HDFS.

Pig introduces PigLatin, a scripting language that lets you use SQL-Like syntax to define your map and reduce steps. 

Pig works better with tez and is much fater that map-reduce in terms of performance. 

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
metadata = LOAD '/user/maria_dev/ml-100k/uitem' USING PigStorage('|') AS (movieID:int, movieTitle:chararray, releaseDate:chararray, videoRelease:chararray, imdbLink:chararray);
```
To fix the date-time [FOREACH,GENERATE]
```
nameLookup = FOREACH metadata GENERATE movieID, movieTitle, ToUnixTime(ToDate(releaseDate, 'dd-MM-yyy')) AS releaseTime;
```
[GROUP,BY,DUMP]
It creates and returns a bag(a tupule of all the values that satisfy)
```
ratingByMovie=GROUP ratings BY movieID;

DUMP ratingsByMovie;
```
[AVG]
```
avgRatings = FOREACH ratingsByMovie GENERATE group AS movieID,AVG(ratings.rating) AS avgRating;

DUMP avgRatings;
```
[DESCRIBE]
Gives table info
```
DESCRIBE ratings
```
[FILTER]
```
goodmovies = FILTER avgRatings BY avgRatings > 4.0;
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