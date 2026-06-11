from typing import Final

# Game configuration constants
SCREEN_WIDTH: Final[int] = 800
SCREEN_HEIGHT: Final[int] = 600
FPS: Final[int] = 60

# Colors in RGB format
BLACK: Final[tuple[int, int, int]] = (0, 0, 0)
WHITE: Final[tuple[int, int, int]] = (255, 255, 255)
RED: Final[tuple[int, int, int]] = (255, 0, 0)
GREEN: Final[tuple[int, int, int]] = (0, 255, 0)
BLUE: Final[tuple[int, int, int]] = (0, 0, 255)

# Game states
class GameState:
    MAIN_MENU: Final[int] = 0
    PLAYING: Final[int] = 1
    GAME_OVER: Final[int] = 2
    PAUSED: Final[int] = 3

# Paths
ASSET_PATH: Final[str] = "assets/"
CONFIG_PATH: Final[str] = "config/settings.json"

# Player settings
PLAYER_START_X: Final[int] = SCREEN_WIDTH // 2
PLAYER_START_Y: Final[int] = SCREEN_HEIGHT // 2
PLAYER_SPEED: Final[float] = 5.0
