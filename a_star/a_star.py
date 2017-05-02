import numpy as np
import pygame
import fire
from node import Node

def search(num_rows=10, num_cols=10, WIDTH=400, HEIGHT=300):
    # Create nodes
    x_spacement = WIDTH // num_rows
    y_spacement = HEIGHT // num_cols
    nodes = [[Node(i, j, x_spacement, y_spacement) for i in range(num_rows)] for j in range(num_cols)]

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

def draw_nodes(surface, nodes):
    for i_nodes in nodes:
        for node in i_nodes:
            pygame.draw.circle(surface, node.color, node.position, node.radius)

if __name__ == '__main__':
    fire.Fire(search)
