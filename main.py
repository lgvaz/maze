import pygame
import fire
import recursive_backtracer
import a_star
import depth_first

def start(search, num_rows=50, num_cols=50, WIDTH=601, HEIGHT=601, render=True):
    ''' Generate and solve mazes.

    Args:
        search (str): Pathfind algorithm to be used. (a_star, depth_first)
        num_rows (int): Number of cells of each column
        num_cols (int): Number of cells of each row
        WIDTH (int): Screen width (Number of pixels)
        HEIGHT (int): Screen height (Number of pixels)
        render (bool): Whether or not to render maze while creating and solving
    '''
    # Create pygame window
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    # Create maze
    maze = recursive_backtracer.create_maze(screen, num_rows, num_cols, render)
    # Use specified algorithm to find solution
    eval(search).search(maze, render)

    while True:
        maze.draw()

if __name__ == '__main__':
    fire.Fire(start)
