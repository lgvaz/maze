import random
from grid import Grid
import time

maze = Grid()
# Define the start of the maze
current = maze.grid[0][0]
current.visited = True
# Stack of visited cells
stack = []
while True:
    # Find unvisited neighbors
    neighbors = maze.unvisited_neighbors(current)
    # If they're neighbors
    if neighbors:
        if len(neighbors) > 1:
            stack.append(current)
        # Select a random neighbor
        r_neighbor = random.choice(neighbors)
        # Remove wall between neighbor and current
        maze.remove_wall(current, r_neighbor)
        # Move to it
        current = r_neighbor
        current.visited = True
    elif stack:
        current = stack.pop()

    maze.draw(current)
