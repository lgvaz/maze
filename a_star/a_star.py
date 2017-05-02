import numpy as np
import pygame
import fire
from node import Node
from utils import COLORS, draw_nodes

def search(num_rows=10, num_cols=10, WIDTH=400, HEIGHT=300):
    # Create nodes
    w_spacement = WIDTH // num_cols
    h_spacement = HEIGHT // num_rows
    nodes = [[Node(i, j, w_spacement, h_spacement)
              for i in range(num_cols)] for j in range(num_rows)]

    # Testing findng_neighbors
    # for i_nodes in nodes:
    #     for node in i_nodes:
    #         node.find_neighbors(nodes, num_rows, num_cols)
    # print(nodes[1][0].neighbors)    
    # Define start and goal
    start = nodes[0][0]
    start.color = COLORS['green']
    goal = nodes[num_rows - 1][num_cols - 1]
    goal.color = COLORS['red']
    # Define unexplored nodes
    open_nodes = []
    open_nodes.append(start)
    # Define exploerd nodes
    closed_nodes = []

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
