import json
import os
from typing import Any, Dict

class ConfigLoader:
    def __init__(self, defaults: Dict[str, Any], path: str = 'settings.json'):
        self.path = path
        self.config = defaults
        self._load_and_merge()

    def _load_and_merge(self) -> None:
        if not os.path.exists(self.path):
            self._save_defaults()
            return
        try:
            with open(self.path, 'r') as f:
                user_cfg = json.load(f)
                self.config.update({k: v for k, v in user_cfg.items() if k in self.config})
        except (json.JSONDecodeError, IOError):
            pass

    def _save_defaults(self) -> None:
        try:
            with open(self.path, 'w') as f:
                json.dump(self.config, f, indent=4)
        except IOError:
            pass

    def get(self, key: str, fallback: Any = None) -> Any:
        return self.config.get(key, fallback)

# Usage example for game settings
def get_game_config() -> ConfigLoader:
    defaults = {
        "resolution": [1920, 1080],
        "vsync": True,
        "target_fps": 144,
        "audio_master": 0.8
    }
    return ConfigLoader(defaults)