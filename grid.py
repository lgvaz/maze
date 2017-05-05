import pygame

class Grid:
    def __init__(self, screen, num_rows, num_cols):
        self.num_rows = num_rows
        self.num_cols = num_cols
        w, h = pygame.display.get_surface().get_size()
        x_square_size = w // num_cols
        y_square_size = h // num_rows
        # Pygame setup
        pygame.init
        self.screen = screen

        self.grid = [[Cell(i, j, x_square_size, y_square_size) for j in range(num_cols)] for i in range(num_rows)]

    def set_start(self, cell):
        self.start = cell

    def set_goal(self, cell):
        self.goal = cell

    def draw(self, highlight_cell=None):
        self.screen.fill(0x212530)
        for row_cells in self.grid:
            for cell in row_cells:
                # Color cells
                if cell is self.start:
                    pygame.draw.rect(self.screen, 0x0000FF, cell.rect)
                elif cell is self.goal:
                    pygame.draw.rect(self.screen, 0xD01037, cell.rect)
                elif cell.final_path == True:
                    pygame.draw.rect(self.screen, 0xDB8B12, cell.rect)
                elif cell.explored == True:
                    pygame.draw.rect(self.screen, 0x34CBB0, cell.rect)
                elif cell.visited == True:
                    pygame.draw.rect(self.screen, 0xD3D5E1, cell.rect)
                # Color highlight_cell differently
                if highlight_cell:
                    pygame.draw.rect(self.screen, 0x10ED4F, highlight_cell.rect)
                # Draw each line of the cell
                if cell.visited == True:
                    for wall, start, end in cell.lines.values():
                        if wall == True:
                            pygame.draw.line(self.screen, 0x212530, start, end)
        # Update display
        pygame.display.flip()
        # Check if close button was pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise ValueError('Window closed')

    def get_size(self):
        return self.num_rows, self.num_cols

    def neighbors(self, cell):
        neighbors = []
        if cell.i > 0:
            neighbors.append(self.grid[cell.i - 1][cell.j])
        if cell.j < self.num_cols - 1:
            neighbors.append(self.grid[cell.i][cell.j + 1])
        if cell.i < self.num_rows - 1:
            neighbors.append(self.grid[cell.i + 1][cell.j])
        if cell.j > 0:
            neighbors.append(self.grid[cell.i][cell.j - 1])
        return neighbors

    def unvisited_neighbors(self, cell):
        return [neighbor for neighbor in self.neighbors(cell) if neighbor.visited == False]

    def valid_neighbors(self, cell):
        i = cell.i
        j = cell.j
        neighbors = []
        # Top neighbor
        if cell.i > 0 and cell.lines['top'][0] == False:
            neighbors.append(self.grid[i - 1][j])
        # Bottom neighbor
        if cell.i < self.num_rows - 1 and cell.lines['bottom'][0] == False:
            neighbors.append(self.grid[i + 1][j])
        # Right neighbor
        if cell.j < self.num_cols - 1 and cell.lines['right'][0] == False:
            neighbors.append(self.grid[i][j + 1])
        # Left neighbor
        if cell.j > 0 and cell.lines['left'][0] == False:
            neighbors.append(self.grid[i][j - 1])
        return neighbors

    def remove_wall(self, cell1, cell2):
        if cell1.i - cell2.i == 1:
            cell1.lines['top'][0] = False
            cell2.lines['bottom'][0] = False
        elif cell1.i - cell2.i == -1:
            cell1.lines['bottom'][0] = False
            cell2.lines['top'][0] = False
        elif cell1.j - cell2.j == 1:
            cell1.lines['left'][0] = False
            cell2.lines['right'][0] = False
        elif cell1.j - cell2.j == -1:
            cell1.lines['right'][0] = False
            cell2.lines['left'][0] = False
        else:
            raise ValueError('Cannot remove walls between non neighbor cells')

    def trace_final_path(self):
        path = []
        current = self.goal
        while current is not self.start:
            path.append(current)
            current.final_path = True
            current = current.parent
        path.append(self.start)
        return path


class Cell:
    def __init__(self, i, j, x_ss, y_ss):
        # Cell identification
        self.i = i
        self.j = j
        self.visited = False
        self.explored = False
        self.final_path = False
        # (Wall, start, end)
        self.lines = {
            'top':      [True,
                         (j * x_ss, i * y_ss),
                         (j * x_ss + x_ss, i * y_ss)],
            'right':    [True,
                         (j * x_ss + x_ss, i * y_ss),
                         (j * x_ss + x_ss, i * y_ss + y_ss)],
            'bottom':   [True,
                         (j * x_ss, i * y_ss + y_ss),
                         (j * x_ss + x_ss, i * y_ss + y_ss)],
            'left':     [True,
                         (j * x_ss, i * y_ss),
                         (j * x_ss, i * y_ss + y_ss)]
        }
        self.rect = (j * x_ss,
                     i * y_ss,
                     x_ss,
                     y_ss)
