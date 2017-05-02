from utils import COLORS
class Node:
    def __init__(self, x, y, w_spacement, h_spacement):
        self.color = COLORS['white']
        self.radius = 10
        self.position = (x * w_spacement + w_spacement // 2,
                         y * h_spacement + h_spacement // 2)
        self.x = x * w_spacement
        self.y = y * h_spacement
