import json
import os
from typing import Any, Dict

class ConfigLoader:
    def __init__(self, path: str, defaults: Dict[str, Any]):
        self.path = path
        self.data = defaults
        self._load()

    def _load(self) -> None:
        if os.path.exists(self.path):
            try:
                with open(self.path, 'r') as f:
                    loaded = json.load(f)
                    self.data.update(loaded)
            except (json.JSONDecodeError, IOError):
                pass

    def get(self, key: str, fallback: Any = None) -> Any:
        return self.data.get(key, fallback)

    def __getitem__(self, key: str) -> Any:
        return self.data[key]

    def sync(self) -> None:
        with open(self.path, 'w') as f:
            json.dump(self.data, f, indent=4)

def get_game_config(overrides: Dict[str, Any] = None) -> ConfigLoader:
    defaults = {
        "fps_limit": 144,
        "vsync": False,
        "resolution": [1920, 1080],
        "graphics_preset": "ultra"
    }
    loader = ConfigLoader("settings.json", defaults)
    if overrides:
        loader.data.update(overrides)
    return loader