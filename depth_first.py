import time


def search(maze):
    start = maze.start
    goal = maze.goal

    visited_cells = []
    visited_cells.append(start)

    while visited_cells:
        current = visited_cells.pop()
        if current.explored == False:
            current.explored = True
            neighbors = maze.valid_neighbors(current)
            visited_cells.extend(neighbors)

            maze.draw(current)
