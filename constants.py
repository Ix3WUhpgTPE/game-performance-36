import math

# Game constants
def get_gravitational_acceleration(scale=1.0):
    """Returns gravitational acceleration based on scale."""
    return 9.81 * scale

# Screen settings
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

# Color definitions
class Colors:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

# Utility functions
def is_point_within_bounds(point, bounds):
    """Check if a point is within provided bounds."""
    x, y = point
    return bounds[0] <= x <= bounds[2] and bounds[1] <= y <= bounds[3]

# Game physics
def calculate_distance(point1, point2):
    """Calculate the distance between two points."""
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)  

# Time management
FPS = 60
FRAME_TIME = 1.0 / FPS
