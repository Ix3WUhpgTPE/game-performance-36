import random
import math

def generate_random_coordinates(x_limit, y_limit):
    return (random.randint(0, x_limit), random.randint(0, y_limit))


def clamp(value, min_value, max_value):
    return max(min(value, max_value), min_value)


def distance(point_a, point_b):
    return math.sqrt((point_b[0] - point_a[0]) ** 2 + (point_b[1] - point_a[1]) ** 2)


def lerp(start, end, t):
    return start + (end - start) * t


def is_within_bounds(point, bounds):
    return bounds[0] <= point[0] <= bounds[2] and bounds[1] <= point[1] <= bounds[3]


def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


def normalize(vector):
    magnitude = math.sqrt(sum(comp ** 2 for comp in vector))
    return tuple(comp / magnitude for comp in vector) if magnitude else (0, 0)
