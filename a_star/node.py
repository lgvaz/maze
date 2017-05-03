from numpy.random import uniform
from utils import COLORS

class Node:
    def __init__(self, i, j, w_spacement, h_spacement, wall_pct):
        # Maybe node is a wall
        if uniform() < wall_pct:
            self.wall = True
            self.color = COLORS['wall']
        else:
            self.wall = False
            self.color = COLORS['node']

        self.radius = 3
        self.parent = None
        # Node idxs
        self.i = i
        self.j = j
        # Circle of rectangle specs
        self.circle = (j * w_spacement + w_spacement // 2,
                         i * h_spacement + h_spacement // 2)
        self.rect = (j * w_spacement, i * h_spacement, w_spacement, h_spacement)

        # Cost from start to this node
        self.g_score = float('inf')
        # Cost from start to goal passing by current node
        self.f_score = float('inf')

    def find_neighbors(self, nodes, num_rows, num_cols):
        self.neighbors = []
        for i_ in range(max(0, self.i - 1), min(self.i + 2, num_rows)):
            for j_ in range(max(0, self.j - 1), min(self.j + 2, num_cols)):
                if i_ == self.i and j_ == self.j:
                    continue
                self.neighbors.append(nodes[i_][j_])
        return self.neighbors
