from typing import Dict, Any, Final
from dataclasses import dataclass

@dataclass(frozen=True)
class GameConfig:
    """Immutable performance parameters for game-performance-36."""
    fps_cap: int
    render_scale: float
    enable_vsync: bool

def get_default_settings() -> Dict[str, Any]:
    """Generates a dict of high-performance preset configurations."""
    return {
        "ultra_perf": GameConfig(fps_cap=144, render_scale=0.75, enable_vsync=False),
        "cinematic": GameConfig(fps_cap=60, render_scale=1.0, enable_vsync=True)
    }

class PerformanceRegistry:
    """Registry for dynamic runtime performance tweaking."""
    def __init__(self) -> None:
        self._cache: Dict[str, GameConfig] = get_default_settings()

    def update_profile(self, name: str, config: GameConfig) -> None:
        """Injects a custom performance profile into the registry."""
        self._cache[name] = config

    def fetch_profile(self, name: str) -> GameConfig:
        """Retrieves requested performance profile by string key."""
        return self._cache.get(name, self._cache["ultra_perf"])

GLOBAL_CONFIG: Final = PerformanceRegistry()