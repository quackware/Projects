import datetime

class Rental:
    def __init__(self,movie):
        self.movie = movie
        #1 week return period
        self.returnDate = datetime.date.today() + datetime.timedelta(days=7)
        