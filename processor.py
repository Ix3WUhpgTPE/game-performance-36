import json
import os
from typing import Any, Dict

class ConfigProcessor:
    def __init__(self, path: str, defaults: Dict[str, Any]):
        self.path = path
        self.defaults = defaults
        self.data = self._load_config()

    def _load_config(self) -> Dict[str, Any]:
        if not os.path.exists(self.path):
            return self.defaults
        try:
            with open(self.path, 'r') as f:
                loaded = json.load(f)
                return {**self.defaults, **loaded}
        except (json.JSONDecodeError, IOError):
            return self.defaults

    def get(self, key: str) -> Any:
        return self.data.get(key, self.defaults.get(key))

    def patch(self, new_settings: Dict[str, Any]) -> None:
        self.data.update(new_settings)
        with open(self.path, 'w') as f:
            json.dump(self.data, f, indent=4)

# Dynamic default configuration injection for game
def initialize_game_settings(file_path: str) -> ConfigProcessor:
    base_defaults = {
        "vsync": True,
        "max_fps": 144,
        "shadow_quality": "medium",
        "audio_channels": 64
    }
    return ConfigProcessor(file_path, base_defaults)