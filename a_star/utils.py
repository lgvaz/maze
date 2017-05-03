import pygame

# Constants
COLORS = {
    'red': (255, 0, 0),
    'green': (20, 230, 20),
    'blue': (121, 166, 217),
    'purple': (200, 0, 255),
    'day9': (255, 167, 26),
    'gray': (38, 50, 56),
    'gray2': (70, 70, 70),
    'white': (240, 240, 240)
}

def draw_nodes(surface, nodes):
    surface.fill(COLORS['gray'])
    for i_nodes in nodes:
        for node in i_nodes:
            pygame.draw.circle(surface, node.color, node.position, node.radius)

def euclidian_distance(node, goal):
    return ((goal.i - node.i)**2 +
            (goal.j - node.j)**2) ** 0.5

def find_best_f(nodes):
    current_best = nodes[0]
    for node in nodes:
        if node.f_score < current_best.f_score:
            current_best = node
    return current_best

def trace_path(start, goal):
    path = []
    current = goal
    while current is not start:
        #current.color = COLORS['purple']
        path.append(current)
        current = current.parent
    return path
