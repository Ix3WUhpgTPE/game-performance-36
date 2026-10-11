import math
from typing import Final

# Precomputed lookup tables for rapid trigonometric operations in gaming engine
# Reducing CPU load by bypassing runtime math function overheads

LOOKUP_PRECISION: Final[int] = 1024

class PerformanceConstants:
    """Static performance acceleration mappings."""
    SIN_TABLE: Final[list[float]] = [
        math.sin(2 * math.pi * i / LOOKUP_PRECISION) 
        for i in range(LOOKUP_PRECISION)
    ]
    COS_TABLE: Final[list[float]] = [
        math.cos(2 * math.pi * i / LOOKUP_PRECISION) 
        for i in range(LOOKUP_PRECISION)
    ]

    @staticmethod
    def fast_sin(angle_rad: float) -> float:
        index = int((angle_rad / (2 * math.pi)) * LOOKUP_PRECISION) % LOOKUP_PRECISION
        return PerformanceConstants.SIN_TABLE[index]

    @staticmethod
    def fast_cos(angle_rad: float) -> float:
        index = int((angle_rad / (2 * math.pi)) * LOOKUP_PRECISION) % LOOKUP_PRECISION
        return PerformanceConstants.COS_TABLE[index]

# Memory-aligned buffer sizes for high-frequency network packets
MAX_PACKET_SIZE: Final[int] = 4096
BUFFER_THRESHOLD: Final[int] = 1024

# Gameloop cycle frequency optimization
TICKS_PER_SECOND: Final[int] = 64
FRAME_DELTA_TARGET: Final[float] = 1.0 / TICKS_PER_SECOND