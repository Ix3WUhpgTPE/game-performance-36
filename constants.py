import math
from typing import Final, Dict, Any

class GameConstants:
    TICKS_PER_SECOND: Final[int] = 60
    PLAYER_MAX_VELOCITY: Final[float] = 12.5
    GRAVITY_SCALAR: Final[float] = 9.81
    
    # Mapping for performance-oriented bitwise status flags
    STATUS_MAP: Final[Dict[str, int]] = {
        'IDLE': 0,
        'MOVING': 1 << 0,
        'JUMPING': 1 << 1,
        'FALLING': 1 << 2,
        'ATTACKING': 1 << 3,
        'STUNNED': 1 << 4
    }

    @classmethod
    def calculate_frame_time_ms(cls, hz: int = 144) -> float:
        return 1000.0 / hz

    @staticmethod
    def pack_entity_state(is_moving: bool, is_attacking: bool) -> int:
        state = 0
        if is_moving: state |= GameConstants.STATUS_MAP['MOVING']
        if is_attacking: state |= GameConstants.STATUS_MAP['ATTACKING']
        return state

# Configuration snapshots for high-performance tick loops
DEFAULT_CONFIG: Dict[str, Any] = {
    'tick_rate': 64,
    'interpolation_buffer': 0.1,
    'net_timeout_ms': 500
}

def get_performance_mode_scalar(latency: int) -> float:
    # Non-linear scaling for resource allocation based on network latency
    return max(0.5, 1.0 - math.log1p(latency) / 10.0)