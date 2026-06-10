import random
import numpy as np

def random_position(bounds):
    return (random.uniform(bounds[0], bounds[1]), random.uniform(bounds[2], bounds[3]))

def distance(point1, point2):
    return np.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def clamp(value, min_value, max_value):
    return max(min(value, max_value), min_value)

def lerp(start, end, t):
    return start + (end - start) * t

def is_within_bounds(point, bounds):
    return bounds[0] <= point[0] <= bounds[1] and bounds[2] <= point[1] <= bounds[3]

if __name__ == '__main__':
    print(random_position((0, 100, 0, 100)))
    print(distance((0, 0), (3, 4)))
    print(clamp(10, 1, 5))
    print(lerp(0, 100, 0.5))
    print(is_within_bounds((50, 50), (0, 100, 0, 100)))