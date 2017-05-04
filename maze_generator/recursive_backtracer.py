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
    # Move to it
    current = r_neighbor
    current.visited = True

    maze.draw()
    time.sleep(.5)
