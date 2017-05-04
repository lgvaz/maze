from grid import Grid

maze = Grid()
current = maze.grid[0][0]
current.visited = True
while True:
    maze.draw()
