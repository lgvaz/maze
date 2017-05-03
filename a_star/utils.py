import pygame

# Constants
COLORS = {
    'background': 0x263238,
    'path': 0xe3b93c,
    'explored': 0x73a2f8,
    'wall': 0xfa4964,
    'node': 0x2c383e,
    'goal': 0xc3e875,
    'final_path': 0x377d42
}

def draw_nodes(surface, nodes):
    surface.fill(COLORS['background'])
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
    path_pos = []
    current = goal
    while current is not start:
        current.color = COLORS['final_path']
        path.append(current)
        path_pos.append(current.position)
        current = current.parent
    return path, path_pos
