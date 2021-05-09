from grid import Grid

grid = Grid(7, 6)
turn = 0
grid.show()
while not grid.game_over():
    selection = -1
    while selection not in grid.possible_moves():
        selection = int(input(f"Player {turn}: pick a column (0-6): "))
    grid.play(turn, selection)
    grid.show()
    grid.score(turn)
    turn = (turn + 1) % 2

