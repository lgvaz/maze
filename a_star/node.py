from utils import COLORS
class Node:
    def __init__(self, x, y, x_spacement, y_spacement):
        self.color = COLORS['white']
        self.radius = 10
        self.position = (x * x_spacement + self.radius,
                         y * y_spacement + self.radius)
        self.x = x * x_spacement
        self.y = y * y_spacement
