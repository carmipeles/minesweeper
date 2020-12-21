from minesweeper import MineSweeper

m = MineSweeper()
m.set_mines(1)
game_over = False
while not game_over:
    m.print()
    x = int(input("enter x:"))
    y = int(input("enter y:"))
    move_type = input("enter 'o' for open, 'f' for flag or a 'd' for discover:")
    game_over = m.move(move_type, x, y)