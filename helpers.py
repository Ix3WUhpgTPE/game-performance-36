import random
import math


def generate_random_position(width, height):
    return (random.randint(0, width), random.randint(0, height))


def calculate_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


def clamp(value, minimum, maximum):
    return max(minimum, min(value, maximum))


def lerp(start, end, t):
    return start + (end - start) * t


def is_point_in_rectangle(point, rect):
    x, y = point
    rect_x, rect_y, rect_width, rect_height = rect
    return rect_x <= x <= rect_x + rect_width and rect_y <= y <= rect_y + rect_height


def normalized_vector(vector):
    length = math.sqrt(vector[0] ** 2 + vector[1] ** 2)
    if length == 0:
        return (0, 0)
    return (vector[0] / length, vector[1] / length)


def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
