import random
from grid import Grid

def create_maze(screen, num_rows, num_cols):
    maze = Grid(screen, num_rows, num_cols)
    # Define the start of the maze
    current = maze.grid[0][0]
    maze.set_start(current)
    current.visited = True
    # Define maze goal
    maze.set_goal(maze.grid[num_rows - 1][num_cols - 1])
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
        # Else maze is done
        else:
            break

        maze.draw(current)
    return maze
