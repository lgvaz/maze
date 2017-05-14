def euclidian_distance(cell, goal):
    return ((goal.i - cell.i)**2 +
            (goal.j - cell.j)**2) ** 0.5

def manhattan_distance(cell, goal):
    return (abs(goal.i - cell.i) +
            abs(goal.j - cell.j))

def find_best_f(cells):
    current_best = cells[0]
    for cell in cells:
        if cell.f_score < current_best.f_score:
            current_best = cell
    return current_best


def search(maze, render):
    # Initial setup
    start = maze.start
    goal = maze.goal
    num_rows, num_cols = maze.get_size()
    # Evaluated cells
    closed_cells = []
    # Discovered cells, that where not evaluated yet
    open_cells = [start]
    # For each cell
    for cells_row in maze.grid:
        for cell in cells_row:
            # Cost from going from the start cell to selected cell (initialize with inf)
            cell.g_score = float('inf')
            # g_score + estimated cost from selected cell to goal
            cell.f_score = float('inf')
    # g_score of start cell is zero
    start.g_score = 0
#    start.f_score = euclidian_distance(start, goal)
    start.f_score = manhattan_distance(start, goal)

    # Main loop
    while open_cells:
        # Select cell with lowest f_score from open_cells
        current = find_best_f(open_cells)
        # Check if current cell is the goal
        if current is goal:
            print('Solution found!')
            break
        # Update evaluated cells
        current.explored = True
        open_cells.remove(current)
        closed_cells.append(current)
        # Check neighbors
        neighbors = maze.valid_neighbors(current)
        for neighbor in neighbors:
            # If neighbor was already explored, skip it
            if neighbor in closed_cells:
                continue
            # Add neighbor to open_cells
            if neighbor not in open_cells:
                open_cells.append(neighbor)
            # g_score using current path
            neighbor_g = current.g_score + 1
            # Test if g_score is better using current path
            if neighbor_g <= neighbor.g_score:
                neighbor.g_score = neighbor_g
                # Keep track of current path
                neighbor.parent = current
                # Calculate f_score
#                neighbor.f_score = neighbor.g_score + euclidian_distance(neighbor, goal)
                neighbor.f_score = neighbor.g_score + manhattan_distance(neighbor, goal)
        if render:
            maze.draw(current)

    # Trace the final path
    final_path = maze.trace_final_path()
