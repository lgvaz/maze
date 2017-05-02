import numpy as np
import pygame
import fire
from node import Node

# Constants
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

def search(WIDTH=400, HEIGHT=300):
    # Pygame setup
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    done = False

    # Create nodes
    nodes = [[Node for i in range(5)] for j in range(5)]
    print(nodes)

    # Main loop
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # Update display
        pygame.display.flip()

    #def draw_grid():

if __name__ == '__main__':
    fire.Fire(search)
