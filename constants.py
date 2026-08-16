from typing import Final

# Game settings constants
SCREEN_WIDTH: Final[int] = 800
SCREEN_HEIGHT: Final[int] = 600
FPS: Final[int] = 60

# Color constants
BLACK: Final[tuple[int, int, int]] = (0, 0, 0)
WHITE: Final[tuple[int, int, int]] = (255, 255, 255)
RED: Final[tuple[int, int, int]] = (255, 0, 0)
GREEN: Final[tuple[int, int, int]] = (0, 255, 0)
BLUE: Final[tuple[int, int, int]] = (0, 0, 255)

# Game state constants
MENU_STATE: Final[str] = 'menu'
PLAYING_STATE: Final[str] = 'playing'
PAUSED_STATE: Final[str] = 'paused'
GAME_OVER_STATE: Final[str] = 'game_over'

# Maximum score constants
MAX_SCORE: Final[int] = 100000

# Speed constants
PLAYER_SPEED: Final[float] = 5.0
ENEMY_SPEED: Final[float] = 3.0

# Miscellaneous settings
GRAVITY: Final[float] = 9.8

def display_constants() -> None:
    """
    Display all constant values for debugging purposes.
    """
    constants = { 'SCREEN_WIDTH': SCREEN_WIDTH, 'SCREEN_HEIGHT': SCREEN_HEIGHT,
                  'FPS': FPS, 'BLACK': BLACK, 'WHITE': WHITE,
                  'RED': RED, 'GREEN': GREEN, 'BLUE': BLUE,
                  'MENU_STATE': MENU_STATE, 'PLAYING_STATE': PLAYING_STATE,
                  'PAUSED_STATE': PAUSED_STATE, 'GAME_OVER_STATE': GAME_OVER_STATE,
                  'MAX_SCORE': MAX_SCORE, 'PLAYER_SPEED': PLAYER_SPEED,
                  'ENEMY_SPEED': ENEMY_SPEED, 'GRAVITY': GRAVITY }
    for name, value in constants.items():
        print(f'{name}: {value}')