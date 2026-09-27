from enum import Enum, unique
from typing import Final

@unique
class PerformanceMetric(Enum):
    FRAME_TIME = "ms"
    GPU_TEMP = "celsius"
    VRAM_USAGE = "mb"
    CPU_LOAD = "percent"

DEFAULT_THRESHOLDS: Final[dict[PerformanceMetric, float]] = {
    PerformanceMetric.FRAME_TIME: 16.6,
    PerformanceMetric.GPU_TEMP: 85.0,
    PerformanceMetric.VRAM_USAGE: 8192.0,
    PerformanceMetric.CPU_LOAD: 90.0,
}

CACHE_TTL_SECONDS: Final[int] = 300
MAX_RETRY_ATTEMPTS: Final[int] = 3

LOG_FORMAT: Final[str] = "%(asctime)s | %(levelname)s | %(message)s"
VERSION: Final[str] = "0.3.6-stable"

class EngineState(Enum):
    IDLE = 0
    INITIALIZING = 1
    BENCHMARKING = 2
    ERROR = -1

TARGET_FPS: Final[int] = 144
BUFFER_SIZE: Final[int] = 1024 * 64