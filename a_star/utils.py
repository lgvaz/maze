import pygame

# Constants
COLORS = {
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'blue': (0, 0, 255),
    'white': (255, 255, 255)
}

def draw_nodes(surface, nodes):
    for i_nodes in nodes:
        for node in i_nodes:
            pygame.draw.circle(surface, node.color, node.position, node.radius)

def euclidian_distance(node, goal):
    return ((goal.position[0] - node.position[0])**2 +
            (goal.position[1] - node.position[1])**2) ** 0.5
