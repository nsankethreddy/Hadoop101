# Map-reduce

Map-reduce is natively written in java but STREAMING allows interfacing to python

mrjob library in python helps in STREAMING
```
def mapper_get_ratings(self, _, line):
    (userID, movieID, rating, timestamp) = line.split('\t')
    yield rating, 1
````

```
def reducer_count_ratings(self, key, values):
    yield key, sum(values)
```

### Putting it all together:

```
from mrjob.job import MRJob
from mrjob.step import MRStep

class RatingsBreakdown(MRJob):
    def steps(self):
        return[ MRStep(mapper=self.mapper_get_ratings, reducer=self.reducer_count_ratings)] 

    def mapper_get_ratings(self, _, line):
    (userID, movieID, rating, timestamp) = line.split('\t')
    yield rating, 1

    def reducer_count_ratings(self, key, values):
    yield key, sum(values)

if __name__ = '__main__':
    RatingsBreakdown.run()
```