import json
import os
from typing import Any, Dict, Optional

class ConfigLoader:
    def __init__(self, defaults: Optional[Dict[str, Any]] = None, config_path: Optional[str] = None):
        if defaults is None:
            defaults = {"resolution": (1920, 1080), "fps_limit": 60, "fullscreen": True, "volume": 0.8, "graphics_quality": "high", "vsync": True}
        self._config = defaults.copy()
        self._load_from_env()
        if config_path and os.path.isfile(config_path):
            self._load_from_file(config_path)
    def _load_from_env(self):
        for key, current in list(self._config.items()):
            env_key = "GAME_" + key.upper()
            if env_key in os.environ:
                val = os.environ[env_key]
                if isinstance(current, bool):
                    self._config[key] = val.lower() in ("true", "1", "yes")
                elif isinstance(current, int):
                    try: self._config[key] = int(val)
                    except ValueError: pass
                elif isinstance(current, float):
                    try: self._config[key] = float(val)
                    except ValueError: pass
                else:
                    self._config[key] = val
    def _load_from_file(self, path):
        try:
            with open(path, "r") as f:
                for k, v in json.load(f).items():
                    if k in self._config:
                        self._config[k] = v
        except:
            pass
    def get(self, key, default=None):
        return self._config.get(key, default)
    def set(self, key, value):
        self._config[key] = value
    def save(self, path):
        with open(path, "w") as f:
            json.dump(self._config, f, indent=2)
    def all(self):
        return self._config.copy()