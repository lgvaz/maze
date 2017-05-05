import pygame
import fire
import recursive_backtracer
import a_star

def start(num_rows=50, num_cols=50, WIDTH=601, HEIGHT=601):
    # Create pygame window
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    # Create maze
    maze = recursive_backtracer.create_maze(screen, num_rows, num_cols)
    # Use a-star to find solution
    a_star.search(maze)

    while True:
        maze.draw()

if __name__ == '__main__':
    fire.Fire(start)
