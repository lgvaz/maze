import pygame

# Constants
COLORS = {
    'background': 0x263238,
    'path': 0xe3b93c,
    'explored': 0x73a2f8,
    'wall': 0xfa4964,
    'node': 0x2c383e,
    'goal': 0xc3e875,
    'current': 0x5d616c,
    'final_path': 0x377d42
}

def draw_nodes(surface, nodes, shape):
    surface.fill(COLORS['background'])
    for i_nodes in nodes:
        for node in i_nodes:
            if shape == 'rect':
                pygame.draw.rect(surface, node.color, node.rect)
            elif shape == 'circle':
                pygame.draw.circle(surface, node.color, node.circle, node.radius)
            else:
                raise ValueError('Format "{}" not implemented'.format(shape))

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
        current.color = COLORS['final_path']
        path.append(current)
        current = current.parent
    start.color = COLORS['final_path']
    path.append(start)
    return path
