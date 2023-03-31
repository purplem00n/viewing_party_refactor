class Person:
    def __init__(self, name, friends):
        self.name = name
        self.friends = friends
        self.watchlist = []
    
    def add_friend(self, friend):
        if friend not in self.friends:
            self.friends.append(friend)

    def add_to_watchlist(self, movie):
        if movie not in self.watchlist:
            self.watchlist.append(movie)