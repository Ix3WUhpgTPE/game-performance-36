import os
import json
from typing import Any, Dict

class GameConfig:
    DEFAULT_SETTINGS = {
        "frame_rate_cap": 144,
        "vsync": True,
        "resolution": [1920, 1080],
        "graphics_preset": "ultra"
    }

    def __init__(self, path: str = "settings.json"):
        self.path = path
        self.data = self._load_data()

    def _load_data(self) -> Dict[str, Any]:
        if not os.path.exists(self.path):
            return self.DEFAULT_SETTINGS
        try:
            with open(self.path, "r") as f:
                loaded = json.load(f)
            return {**self.DEFAULT_SETTINGS, **loaded}
        except (json.JSONDecodeError, IOError):
            return self.DEFAULT_SETTINGS

    def get(self, key: str) -> Any:
        return self.data.get(key, self.DEFAULT_SETTINGS.get(key))

    def __getattr__(self, name: str) -> Any:
        return self.get(name)

def initialize_game_config() -> GameConfig:
    instance = GameConfig()
    return instance