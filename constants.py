from enum import IntEnum
from typing import Final, Dict, Any

class GameTick(IntEnum):
    IDLE = 0
    TICK_FAST = 16
    TICK_NORMAL = 32
    TICK_SLOW = 64

class PerformanceMetrics:
    THRESHOLD_MS: Final[float] = 16.67
    BUFFER_CAPACITY: Final[int] = 1024

    @staticmethod
    def get_tier(frame_time: float) -> str:
        tiers = {
            0.0: 'OPTIMAL',
            16.6: 'STABLE',
            33.3: 'DEGRADED',
            float('inf'): 'CRITICAL'
        }
        for limit in sorted(tiers.keys()):
            if frame_time <= limit:
                return tiers[limit]
        return 'UNKNOWN'

DEFAULT_CONFIG: Final[Dict[str, Any]] = {
    "version": "1.0.0-beta",
    "engine": "quantum-mesh",
    "telemetry_enabled": True,
    "priority_levels": {v.name: v.value for v in GameTick}
}

def derive_frequency(tick_rate: GameTick) -> float:
    return 1000.0 / tick_rate if tick_rate > 0 else 0.0