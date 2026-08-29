import json
import os
from copy import deepcopy
def deep_merge(base, override):
    result = deepcopy(base)
    for key, value in override.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = value
    return result
class ConfigLoader:
    def __init__(self, config_file="config.json"):
        self.config_file = config_file
        self.defaults = {
            "game": {
                "title": "GamePerformance36",
                "version": "1.0"
            },
            "video": {
                "resolution": "1920x1080",
                "fullscreen": False,
                "fps_limit": 60,
                "quality": "medium"
            },
            "audio": {
                "master_volume": 1.0,
                "effects": True,
                "music": True
            },
            "controls": {
                "sensitivity": 1.0,
                "invert_y": False
            }
        }
        self.config = deepcopy(self.defaults)
        self._load_config()
    def _load_config(self):
        if os.path.isfile(self.config_file):
            try:
                with open(self.config_file, "r", encoding="utf-8") as f:
                    user_config = json.load(f)
                self.config = deep_merge(self.defaults, user_config)
            except (json.JSONDecodeError, OSError):
                self.config = deepcopy(self.defaults)
        else:
            self._save_config()
    def _save_config(self):
        with open(self.config_file, "w", encoding="utf-8") as f:
            json.dump(self.config, f, indent=2)
    def get(self, key, default=None):
        keys = key.split(".")
        current = self.config
        for k in keys:
            if isinstance(current, dict) and k in current:
                current = current[k]
            else:
                return default
        return current
    def set(self, key, value):
        keys = key.split(".")
        current = self.config
        for k in keys[:-1]:
            if k not in current or not isinstance(current[k], dict):
                current[k] = {}
            current = current[k]
        current[keys[-1]] = value
        self._save_config()
    def __getattr__(self, name):
        if name in self.config:
            return self.config[name]
        raise AttributeError(f"'ConfigLoader' object has no attribute '{name}'")
    def reload(self):
        self.config = deepcopy(self.defaults)
        self._load_config()