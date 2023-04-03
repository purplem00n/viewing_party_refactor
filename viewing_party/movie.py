import datetime

class Movie:
    def __init__(self, name, genre, rating, release_year):
        self.name = name
        self.genre = genre
        self.rating = rating
        self.release_year = release_year

    def years_since_release(self):
        today = datetime.date.today()
        return today.year - self.release_year