import random
from spot import Spot

class MineSweeper(object):
    def __init__(self, total_mines=10, size=10):
        if total_mines > size*size:
            raise ValueError
        self.total_mines = total_mines
        self.size = size
        for i in range(size):
            for j in range(size):
                Spot(i, j, False)
        self.spots = Spot.spots

    def set_mines(self):
        # TODO: set mines only after the first move
        l = list(self.spots.values())
        random.shuffle(l)
        for s in l[:self.total_mines]:
            s.is_mine = True

    def click(self, x, y):
        self.spots[(x,y)].reveal()
        if self.spots[(x,y)].is_mine:
            print("game over!!!")
            return False
        return True

    def toggle_flag(self, x, y):
        self.spots[(x,y)].toggle_flag()
    
    def discover(self, x, y):
        self.spots[(x,y)].discover()

    def print(self):
        for i in range(self.size):
            print([s.print() for s in [self.spots[(i,j)] for j in range(self.size)]])
        print("")
        print("~~~~~~~~~~~~~~~~~~~~~")
        print("")