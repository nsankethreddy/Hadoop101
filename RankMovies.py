from mrjob.job import MRJob
from mrjob.step import MRStep


class RankMovies(MRJob):
    def steps(self):
        return[MRStep(mapper=self.mapper_get_movieIDs, reducer=self.reducer_count_movieIDs)]

    def mapper_get_movieIDs(self, _, line):
    (userID, movieID, rating, timestamp) = line.split('\t')
    yield movieID, 1

    def reducer_count_movieIDs(self, key, values):
    yield key, sum(values)


if __name__ = '__main__':
    RankMovies.run()
