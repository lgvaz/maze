import random
from grid import Grid
import time

maze = Grid()
# Define the start of the maze
current = maze.grid[0][0]
current.visited = True
while True:
    # Find unvisited neighbors
    neighbors = maze.unvisited_neighbors(current)
    # Select a random neighbor
    r_neighbor = random.choice(neighbors)
    # Remove wall between neighbor and current
    print('Current ({}/{})'.format(current.i, current.j))
    print('neighbo ({}/{})'.format(r_neighbor.i, r_neighbor.j))
    maze.remove_wall(current, r_neighbor)
    # Move to it
    current = r_neighbor
    current.visited = True

    maze.draw()
    time.sleep(.5)
