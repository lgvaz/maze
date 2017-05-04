def euclidian_distance(cell, goal):
    return ((goal.i - cell.i)**2 +
            (goal.j - cell.j)**2) ** 0.5

def find_best_f(nodes):
    current_best = nodes[0]
    for node in nodes:
        if node.f_score < current_best.f_score:
            current_best = node
    return current_best

def search(maze):
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
    start.f_score = euclidian_distance(start, goal)

    # Main loop
    #while open_cells:
        # Select cell with lowest f_score from open_cells
    current = find_best_f(open_cells)
    # Check if current cell is the goal
    if current is goal:
        print('DONE!')
    # Update evaluated cells
    open_cells.remove(current)
    closed_cells.append(current)
    # Check neighbors
    neighbors = maze.valid_neighbors(current)
    for neighbor in neighbors:
        # If neighbor was already explored, skip it
        if neighbor in closed_cells:
            continue
        # g_score using current path
        neighbor_g = current.g_score + 1
        if neighbor_g < neighbor.g_score:
            neighbor.g_score = neighbor_g
            # Keep track of current path
            neighbor.parent = current
