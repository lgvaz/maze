from grid import Grid

maze = Grid()
while True:
    current = maze.grid[0][0]
    current.visited = True
    maze.draw()
