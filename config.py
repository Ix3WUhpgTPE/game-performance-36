import json
import os
from typing import Any, Dict

class GameConfig:
    def __init__(self, defaults: Dict[str, Any], path: str = 'settings.json'):
        self.path = path
        self.data = defaults.copy()
        self._load()

    def _load(self) -> None:
        if os.path.exists(self.path):
            try:
                with open(self.path, 'r') as f:
                    loaded = json.load(f)
                    self.data.update(loaded)
            except (json.JSONDecodeError, IOError):
                pass

    def __getitem__(self, key: str) -> Any:
        return self.data.get(key)

    def save(self) -> None:
        with open(self.path, 'w') as f:
            json.dump(self.data, f, indent=4)

    def __getattr__(self, item: str) -> Any:
        return self.data.get(item)

def get_config() -> GameConfig:
    defaults = {
        "fps_limit": 144,
        "vsync": True,
        "resolution": [1920, 1080],
        "graphics_preset": "ultra"
    }
    return GameConfig(defaults)