import pygame

class Grid:
    def __init__(self, num_rows=10, num_cols=10, WIDTH=601, HEIGHT=601):
        self.num_rows = num_rows
        self.num_cols = num_cols
        x_square_size = WIDTH // num_cols
        y_square_size = HEIGHT // num_rows
        # Pygame setup
        pygame.init
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

        self.grid = [[Cell(i, j, x_square_size, y_square_size) for j in range(num_cols)] for i in range(num_rows)]

    def draw(self):
        for row_cells in self.grid:
            for cell in row_cells:
                # Draw square if visited
                if cell.visited == True:
                    pygame.draw.rect(self.screen, (0, 200, 0, 100), cell.rect)
                # Draw each line of the cell
                for wall, start, end in cell.lines.values():
                    if wall == True:
                        pygame.draw.line(self.screen, 0xFFFFFF, start, end)
        # Update display
        pygame.display.flip()
        # Check if close button was pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise ValueError('Window closed')

    def neighbors(self, cell):
        neighbors = []
        if cell.i > 0:
            neighbors.append(self.grid[cell.i - 1][cell.j])
        if cell.j < self.num_cols - 1:
            neighbors.append(self.grid[cell.i][cell.j + 1])
        if cell.i < self.num_rows:
            neighbors.append(self.grid[cell.i + 1][cell.j])
        if cell.j > 0:
            neighbors.append(self.grid[cell.i][cell.j - 1])
        return neighbors


class Cell:
    def __init__(self, i, j, x_ss, y_ss):
        # Cell identification
        self.i = i
        self.j = j
        self.visited = False
        # (Wall, start, end)
        self.lines = {
            'top':      (True,
                         (j * x_ss, i * y_ss),
                         (j * x_ss + x_ss, i * y_ss)),
            'right':    (True,
                         (j * x_ss + x_ss, i * y_ss),
                         (j * x_ss + x_ss, i * y_ss + y_ss)),
            'bottom':   (True,
                         (j * x_ss, i * y_ss + y_ss),
                         (j * x_ss + x_ss, i * y_ss + y_ss)),
            'left':     (True,
                         (j * x_ss, i * y_ss),
                         (j * x_ss, i * y_ss + y_ss))
        }
        self.rect = (j * x_ss,
                     i * y_ss,
                     x_ss,
                     y_ss)


if __name__ == '__main__':
    my_maze = Grid()
    print(my_maze.neighbors(my_maze.grid[1][0]))
    while True:
        my_maze.draw()
