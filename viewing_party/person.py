class Person:
    def __init__(self, name, friends):
        self.name = name
        self.friends = friends
        self.watchlist = []
        self.watched = []
    
    def add_friend(self, friend):
        if friend not in self.friends:
            self.friends.append(friend)

    def add_to_watchlist(self, movie):
        if movie not in self.watchlist:
            self.watchlist.append(movie)

    def add_to_watched(self, movie):
        '''Add movie to watched if not already watched
        and remove the movie from watchlist.'''
        if movie not in self.watched:
            self.watched.append(movie)
        if movie in self.watchlist:
            self.watchlist.remove(movie)

    def user_unique_watched(self):
        friends_watched = []
        for friend in self.friends:
            friends_watched.extend(friend.watched)
        user_unique_watched = set(self.watched) - set(friends_watched)
        return list(user_unique_watched)
    # this doesn't work because friend in friend.watched is a string of that 
    # friends name, not the object.