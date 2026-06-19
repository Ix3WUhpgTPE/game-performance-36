FPS_LIMIT = 60

# Game settings
DEFAULT_RESOLUTION = (1920, 1080)
DEFAULT_FOV = 90
DEFAULT_VOLUME = 0.5

# Color constants
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_RED = (255, 0, 0)
COLOR_GREEN = (0, 255, 0)
COLOR_BLUE = (0, 0, 255)

# Speed and movement constants
PLAYER_SPEED = 5.0
ENEMY_SPEED = 3.0
BULLET_SPEED = 12.0

# Game state constants
STATE_MENU = 'menu'
STATE_PLAYING = 'playing'
STATE_PAUSED = 'paused'
STATE_GAMEOVER = 'gameover'

# Performance related constants
MAX_ACTIVE_PARTICLES = 1000
FRAME_TIME = 1.0 / FPS_LIMIT

# Resource paths
TEXTURE_PATH = 'assets/textures/'
SOUND_PATH = 'assets/sounds/'

# Optimization constants
USE_SPRITE_BATCHING = True
ENABLE_OBJECT_POOLING = True