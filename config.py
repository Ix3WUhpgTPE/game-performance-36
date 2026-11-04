from typing import Dict, Any, Final
from dataclasses import dataclass

@dataclass(frozen=True)
class EngineConfig:
    """Immutable configuration container for the game engine parameters."""
    fps_limit: int = 144
    use_vulkan: bool = True
    buffer_size: int = 4096

def get_performance_profiles() -> Dict[str, EngineConfig]:
    """Generates a mapping of hardware presets to configuration objects."""
    return {
        "ultra": EngineConfig(fps_limit=240, use_vulkan=True, buffer_size=8192),
        "potato": EngineConfig(fps_limit=30, use_vulkan=False, buffer_size=1024)
    }

class ConfigLoader:
    """Unorthodox loader that treats configuration as a fluid state."""
    def __init__(self, settings: Dict[str, Any]) -> None:
        self._data: Final = settings

    def get_setting(self, key: str, default: Any = None) -> Any:
        """Retrieve configuration value with fallback mechanism."""
        return self._data.get(key, default)

    def __repr__(self) -> str:
        return f"<ConfigLoader keys={list(self._data.keys())}>"