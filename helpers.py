import random
import math

def calculate_distance(point_a, point_b):
    return math.sqrt((point_b[0] - point_a[0]) ** 2 + (point_b[1] - point_a[1]) ** 2)

def choose_random_item(items):
    return random.choice(items)

def clamp(value, min_value, max_value):
    return max(min_value, min(value, max_value))

def is_point_in_bounds(point, bounds):
    return bounds[0][0] <= point[0] <= bounds[1][0] and bounds[0][1] <= point[1] <= bounds[1][1]

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def subtract(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def normalize(self):
        length = self.length()
        return Vector(self.x / length, self.y / length) if length > 0 else Vector(0, 0)