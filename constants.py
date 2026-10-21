from enum import IntEnum
from typing import Dict, Final

class PerformanceTier(IntEnum):
    POTATO = 0
    CONSOLE = 1
    MID_RANGE = 2
    ENTHUSIAST = 3
    GOD_MODE = 4

GAME_RESOLUTION_PRESETS: Final[Dict[str, tuple[int, int]]] = {
    'ultra_low': (800, 600),
    'hd': (1280, 720),
    'full_hd': (1920, 1080),
    'qhd': (2560, 1440),
    '4k': (3840, 2160)
}

FRAME_BUDGET_MAP: Final[Dict[PerformanceTier, float]] = {
    PerformanceTier.POTATO: 33.33,
    PerformanceTier.CONSOLE: 16.67,
    PerformanceTier.MID_RANGE: 11.11,
    PerformanceTier.ENTHUSIAST: 6.94,
    PerformanceTier.GOD_MODE: 4.17
}

def get_frame_budget(tier: PerformanceTier) -> float:
    return FRAME_BUDGET_MAP.get(tier, 16.67)

class ConfigDefaults:
    DEFAULT_FPS_CAP = 60
    V_SYNC_ENABLED = True
    ASYNC_LOADING = True
    MAX_SHADER_CACHE_SIZE_MB = 1024