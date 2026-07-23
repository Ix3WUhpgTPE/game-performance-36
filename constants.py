from typing import Final

# Constants used throughout the game

BASE_HEALTH: Final[int] = 100
BASE_MANA: Final[int] = 50
BASE_ARMOR: Final[int] = 10

# Game settings constants

SCREEN_WIDTH: Final[int] = 1280
SCREEN_HEIGHT: Final[int] = 720
FPS: Final[int] = 60

# Levels constants
LEVELS: Final[list[str]] = [
    'Beginner',
    'Intermediate',
    'Expert',
    'Legendary'
]

# Scoring constants
POINTS_PER_KILL: Final[int] = 100
POINTS_PER_OBJECTIVE: Final[int] = 500

# Player action constants
MOVE_UP: Final[str] = 'W'
MOVE_DOWN: Final[str] = 'S'
MOVE_LEFT: Final[str] = 'A'
MOVE_RIGHT: Final[str] = 'D'

# This module provides constant values for configurations.