import random
from spot import Spot


class MineSweeper(object):
    def __init__(self, size=10):
        self.size = size
        for i in range(size):
            for j in range(size):
                Spot(i, j, False)
        self.spots = Spot.spots

    def set_mines(self, count=10):
        # TODO: set mines only after the first move
        if count > self.size*self.size:
            raise ValueError
        l = list(self.spots.values())
        random.shuffle(l)
        for s in l[:count]:
            s.is_mine = True

    def move(self, move_type, x, y):
        game_over = False
        if move_type == 'o':
            game_over = self.click(x, y)
        elif move_type == 'f':
            self.toggle_flag(x, y)
        elif move_type == 'd':
            self.discover(x, y)
        else:
            print("invalid option, please try again.")
        if all(s.revealed or (s.is_mine and s.is_flagged) for s in self.spots.values()):
            print("good game!!")
            game_over = True
        return game_over

    def click(self, x, y):
        self.spots[(x, y)].reveal()
        if self.spots[(x, y)].is_mine:
            print("game over!!!")
            return True
        return False

    def toggle_flag(self, x, y):
        self.spots[(x, y)].toggle_flag()

    def discover(self, x, y):
        self.spots[(x, y)].discover()

    def print(self):
        for i in range(self.size):
            print([s.print() for s in [self.spots[(i, j)]
                                       for j in range(self.size)]])
        print("")
        print("~~~~~~~~~~~~~~~~~~~~~")
        print("")
