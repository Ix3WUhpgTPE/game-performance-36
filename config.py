import json
import os
from typing import Any, Dict

class GameConfig:
    def __init__(self, config_path: str, defaults: Dict[str, Any]):
        self.path = config_path
        self.data = defaults
        self._load_and_merge()

    def _load_and_merge(self) -> None:
        if os.path.exists(self.path):
            try:
                with open(self.path, 'r') as f:
                    user_data = json.load(f)
                    self.data.update(user_data)
            except (json.JSONDecodeError, IOError):
                pass

    def get(self, key: str, fallback: Any = None) -> Any:
        return self.data.get(key, fallback)

    def __getitem__(self, key: str) -> Any:
        return self.data[key]

def load_performance_settings(path: str = 'settings.json') -> GameConfig:
    defaults = {
        "frame_cap": 144,
        "vsync": False,
        "texture_quality": "ultra",
        "raytracing": False
    }
    return GameConfig(path, defaults)