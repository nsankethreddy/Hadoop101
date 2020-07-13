from mrjob.job import MRJob
from mrjob.step import MRStep


class RankMovies(MRJob):
    def steps(self):
        return[MRStep(mapper=self.mapper_get_movieIDs, reducer=self.reducer_count_movieIDs), MRStep(reducer=self.reducer_sort)]

    def mapper_get_movieIDs(self, _, line):
        (userID, movieID, rating, timestamp) = line.split('\t')
        yield movieID, 1

    def reducer_count_movieIDs(self, key, values):
        yield str(sum(values)).zfill(5), key

    def reducer_sort(self, key, values):
        for value in values:
            yield value, key
            


if __name__ == '__main__':
    RankMovies.run()
