class Spot(object):
    MINE_SYMBOL = "*"
    FLAG_SYMBOL = "!"
    CLOSE_SYMBOL = "_"
    spots = {}

    def __init__(self, x, y, mine):
        Spot.spots.update({(x, y): self})
        self.revealed = False
        self.x = x
        self.y = y
        self.is_mine = mine
        self.is_flagged = False

    @property
    def neibors(self):
        x = self.x
        y = self.y
        return [Spot.spots.get((i, j)) for (i, j) in [(x-1, y-1), (x-1, y), (x-1, y+1),
                                                      (x, y-1), (x, y+1),
                                                      (x+1, y-1), (x+1, y), (x+1, y+1)]
                                                      if Spot.spots.get((i,j))]

    @property
    def content(self):
        return self.MINE_SYMBOL if self.is_mine else sum([1 for n in self.neibors if n.is_mine])

    def reveal(self):
        if self.revealed or self.is_flagged:
            return
        self.revealed = True
        if self.content == 0:
            for s in self.neibors:
                s.reveal()

    def toggle_flag(self):
        self.is_flagged = not self.is_flagged

    def discover(self):
        flag_count = sum([1 for n in self.neibors if n.is_flagged])
        if flag_count < self.content:
            print("not enough flags")
        if flag_count == self.content:
            for n in self.neibors:
                n.reveal()

    def print(self):
        if self.is_flagged:
            return self.FLAG_SYMBOL
        if self.revealed:
            return str(self.content)
        return self.CLOSE_SYMBOL
