import numpy as np
import pygame
import fire
from node import Node
from utils import draw_nodes

def search(num_rows=10, num_cols=10, WIDTH=400, HEIGHT=300):
    # Create nodes
    w_spacement = int((WIDTH)/ num_cols)
    h_spacement = int((HEIGHT)/ num_rows)
    nodes = [[Node(i, j, w_spacement, h_spacement) for i in range(num_cols)] for j in range(num_rows)]
    print(nodes)
    # Define start and goal

    # Pygame setup
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    done = False
    # Main loop
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # Update display
        draw_nodes(screen, nodes)
        pygame.display.flip()

if __name__ == '__main__':
    fire.Fire(search)
