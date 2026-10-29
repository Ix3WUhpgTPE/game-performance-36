import json
import os
from typing import Any, Dict

class ConfigLoader:
    def __init__(self, defaults: Dict[str, Any], config_path: str = 'settings.json'):
        self.path = config_path
        self.data = defaults.copy()
        self._load_from_disk()

    def _load_from_disk(self) -> None:
        if os.path.exists(self.path):
            try:
                with open(self.path, 'r') as f:
                    disk_data = json.load(f)
                    self.data.update(disk_data)
            except (json.JSONDecodeError, IOError):
                pass

    def __getitem__(self, key: str) -> Any:
        return self.data.get(key)

    def __repr__(self) -> str:
        return f"<ConfigLoader({len(self.data)} keys)>"

def get_game_config() -> ConfigLoader:
    defaults = {
        "resolution": [1920, 1080],
        "vsync": True,
        "target_fps": 144,
        "debug_mode": False
    }
    return ConfigLoader(defaults)