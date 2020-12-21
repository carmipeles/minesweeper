from minesweeper import MineSweeper

m = MineSweeper()
m.set_mines()
game_over = False
while not game_over:
    m.print()
    x = int(input("enter x:"))
    y = int(input("enter y:"))
    move = input("enter 'o' for open, 'f' for flag or a 'd' for discover:")
    if move == 'o':
        game_over = m.click(x, y)
    elif move == 'f':
        m.toggle_flag(x, y)
    elif move == 'd':
        m.discover(x, y)
    else:
        print("invalid option, please try again.")
