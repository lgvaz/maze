def search(maze, render):
    start = maze.start
    goal = maze.goal
    # Keep track of cells left to explore
    open_cells = [start]
    
    while open_cells:
        # Move to new cell
        current = open_cells.pop()
        if current is goal:
            print('Solution found!')
            maze.trace_final_path()
            break
        # Don't go to already explored cells
        if current.explored == False:
            current.explored = True
            neighbors = maze.valid_neighbors(current)
            for neighbor in neighbors:
                if neighbor.explored == False:
                    open_cells.append(neighbor)
                    neighbor.parent = current
            if render:
                maze.draw(current)
