class Game:

    all = []

    def __init__(self, title):
        if not title:
            raise Exception
        self._title = title
        Game.all.append(self)
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        raise Exception

    def results(self):
        return [result for result in Result.all if result.game == self]

    def players(self):
        return list(set(result.player for result in self.results()))

    def average_score(self, player):
        scores = 0
        for result in self.results():
            if result.player == player:
                scores += result.score
        return scores / len(self.results())
        

class Player:

    all = []

    def __init__(self, username):
        if len(username) < 2 or len(username) > 16:
            raise Exception
        self._username = username
        Player.all.append(self)
    
    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, value):
        if not isinstance(value, str):
            raise Exception
        self._username = value

    def results(self):
        return [result for result in Result.all if result.player == self]

    def games_played(self):
        return list(set(result.game for result in self.results()))

    def played_game(self, game):
        for result in self.results():
            if result.game == game:
                return True
        return False
            
    def num_times_played(self, game):
        count = 0
        for result in self.results():
            if result.game == game:
                count += 1
        return count

class Result:

    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        if not isinstance(score, int):
            raise Exception
        self._score = score
        Result.all.append(self)
    

    @property
    def score(self):
        return self._score
    
    





