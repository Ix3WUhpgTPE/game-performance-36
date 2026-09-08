from typing import Dict, Any, Union
from dataclasses import dataclass

@dataclass(frozen=True)
class EngineConfig:
    """Immutable configuration for the gaming engine render pipeline."""
    fps_cap: int
    resolution: tuple[int, int]
    vsync_enabled: bool

def load_defaults() -> EngineConfig:
    """Factory for default engine settings initialization."""
    return EngineConfig(fps_cap=144, resolution=(1920, 1080), vsync_enabled=True)

class ConfigRegistry:
    """Dynamic registry for runtime performance tuning parameters."""
    def __init__(self) -> None:
        self._store: Dict[str, Union[int, float, str]] = {"load_factor": 0.8}

    def update_factor(self, key: str, value: Union[int, float]) -> None:
        """Updates internal performance metrics with strict typing."""
        self._store[key] = value

    def get_factor(self, key: str) -> Union[int, float, str, None]:
        """Retrieves requested performance tuning parameter value."""
        return self._store.get(key)

def validate_scaling(factor: float) -> bool:
    """Validation logic for resolution scaling parameters."""
    return 0.1 <= factor <= 2.0