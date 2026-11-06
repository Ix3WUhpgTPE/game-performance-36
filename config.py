import json
import os
from typing import Any, Dict

class ConfigLoader:
    def __init__(self, path: str = 'settings.json', defaults: Dict[str, Any] = None):
        self.path = path
        self.defaults = defaults or {}
        self.data = self._initialize()

    def _initialize(self) -> Dict[str, Any]:
        if not os.path.exists(self.path):
            return self.defaults
        try:
            with open(self.path, 'r') as f:
                loaded = json.load(f)
                return {**self.defaults, **loaded}
        except (json.JSONDecodeError, IOError):
            return self.defaults

    def get(self, key: str, fallback: Any = None) -> Any:
        return self.data.get(key, fallback)

    def __getitem__(self, key: str) -> Any:
        return self.data[key]

    def reload(self) -> None:
        self.data = self._initialize()

def get_game_config():
    defaults = {
        "fps_limit": 144,
        "vsync": True,
        "render_scale": 1.0,
        "debug_mode": False
    }
    return ConfigLoader('config.json', defaults=defaults)