import random
from grid import Grid


def create_maze(screen, mode, num_rows, num_cols, render):
    ''' Growing tree algorithm.
    Can behave like "recursive backtracking" or almost like "Prim's"
    with little change.
    '''
    maze = Grid(screen, num_rows, num_cols)
    # Define the start of the maze
    maze.set_start(maze.grid[0][0])
    current = maze.grid[random.randrange(num_rows)][random.randrange(num_cols)]
    current.visited = True
    # Define maze goal
    maze.set_goal(maze.grid[num_rows - 1][num_cols - 1])
    # Stack of visited cells
    stack = []
    while True:
        # Find unvisited neighbors
        neighbors = maze.unvisited_neighbors(current)
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
            if mode == 'prim':
                current = stack.pop(random.randrange(len(stack)))
            elif mode == 'backtracker':
                current = stack.pop()
        # Else maze is done
        else:
            break
        if render:
            maze.draw(current)

    return maze
