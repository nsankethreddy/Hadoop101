from pyspark.sql import SparkSession
from pyspark.ml.recommendation import ALS
from pyspark.sql import Row
from pyspark.sql.functions import lit

# Load up movie ID -> movie name dictionary

def loadMovieNames():
    movieNames = {}
    with open("ml-100k/u.item") as f:
        for line in f:
            fields = line.split('|')
            movieNames[int(fields[0])] = fields[1].decode('ascii','ignore')
    return movieNames

#convert u.data lines into (userID, movieID, rating)rows

def parseInput(line):
    fields = line.split()
    return Row(userID = int(fields[0]), movieID = int(fields[1]), rating = float(fields[2]))