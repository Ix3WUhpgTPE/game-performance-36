import random
import math

def calculate_distance(point1, point2):
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

def generate_random_position(bound_x, bound_y):
    return (random.uniform(0, bound_x), random.uniform(0, bound_y))

def clamp(value, min_value, max_value):
    return max(min(value, max_value), min_value)

def interpolate(start, end, factor):
    return start + (end - start) * factor

def lerp_color(color1, color2, factor):
    return (
        int(interpolate(color1[0], color2[0], factor)),
        int(interpolate(color1[1], color2[1], factor)),
        int(interpolate(color1[2], color2[2], factor))
    )

def scale_vector(vector, scale):
    return (vector[0] * scale, vector[1] * scale)

def angle_between_vectors(v1, v2):
    dot_product = v1[0] * v2[0] + v1[1] * v2[1]
    mag_v1 = math.sqrt(v1[0] ** 2 + v1[1] ** 2)
    mag_v2 = math.sqrt(v2[0] ** 2 + v2[1] ** 2)
    return math.acos(dot_product / (mag_v1 * mag_v2))