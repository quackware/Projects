from collections import defaultdict

import string, movie, rental

class Store:
    def __init__(self):
        self.movieInventory = defaultdict(string)
        
    def addMovie(self,newMovie):
        self.movieInventory[newMovie.name] = newMovie
        
    def rentMovie(self,movieName):
        if movieName in self.movieInventory:
            movie = self.movieInventory[movieName]
            if movie.stock == 0:
                raise NoInventory("No inventory for movie " + movieName)
            else:
                movie.stock -= 1
                rental = rental.Rental(movie)
                return rental
        else:
            raise NoMovie("No movie named " + movieName + " exists")
            
        
class NoInventory(Exception):
    def __init__(self,message):
        self.message = message
        
    def __str__(self):
        return self.message

class NoMovie(Exception):
    def __init__(self,message):
        self.message = message
        
    def __str__(self):
        return self.message