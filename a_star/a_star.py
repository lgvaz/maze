import numpy as np
import pygame
import fire
from node import Node
from utils import *
import time

def search(num_rows=30, num_cols=30, WIDTH=800, HEIGHT=600):
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
    # Define start and goal node
    start = nodes[0][0]
    goal = nodes[num_rows - 1][num_cols - 1]
    # Define start and goal attributes
    start.color = COLORS['green']
    goal.color = COLORS['red']
    start.g_score = 0
    start.f_score = start.g_score + euclidian_distance(start, goal)
    # Define unexplored nodes
    open_nodes = []
    open_nodes.append(start)
    # Define explored nodes
    closed_nodes = []

    # Pygame setup
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    done = False
    # Main loop
    while not done:
        # Find the best node to expand
        if len(open_nodes) > 0:
            current = find_best_f(open_nodes)
            current.color = COLORS['red']
        else:
            print("Failure!")
            break
        # Check if current node is the goal
        if current is goal:
            print("Done!")
            break

        #
        open_nodes.remove(current)
        closed_nodes.append(current)
        # Begin exploring current neighbors
        neighbors = current.find_neighbors(nodes, num_rows, num_cols)
        for neighbor in neighbors:
            # Ignore neighbor which is already evaluated
            if neighbor in closed_nodes:
                continue
            # Find g score through current path
            neighbor_g = current.g_score + 1
            # Compare new g score with previous one
            if neighbor_g < neighbor.g_score:
                neighbor.g_score = neighbor_g
                neighbor.parent = current
            # Calculate f-score
            neighbor.f_score = neighbor.g_score + euclidian_distance(neighbor, goal)
            # Added neighbor to open_nodes if it isn't present
            if neighbor not in open_nodes:
                open_nodes.append(neighbor)
                neighbor.color = COLORS['blue']

        # Check if close button was pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        # Update display
        draw_nodes(screen, nodes)
        pygame.display.flip()

        time.sleep(0.2)

    # Don't close screen after the code was executed, instead wait for user to close
    while not done:
        # Check if close button was pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

    # for nodes_ in nodes:
    #     print('\n')
    #     for node in nodes_:
    #         print(node.g_score, end='|')


if __name__ == '__main__':
    fire.Fire(search)
