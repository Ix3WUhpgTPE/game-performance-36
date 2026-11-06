import json
import os
from typing import Any, Dict

class ConfigLoader:
    def __init__(self, path: str = 'settings.json'):
        self.path = path
        self.defaults = {
            'fps_limit': 144,
            'vsync': True,
            'resolution': [1920, 1080],
            'debug_mode': False
        }

    def __getitem__(self, key: str) -> Any:
        return self.load().get(key, self.defaults.get(key))

    def load(self) -> Dict[str, Any]:
        if not os.path.exists(self.path):
            return self.defaults
        try:
            with open(self.path, 'r') as f:
                return {**self.defaults, **json.load(f)}
        except (json.JSONDecodeError, IOError):
            return self.defaults

    def save(self, data: Dict[str, Any]) -> None:
        with open(self.path, 'w') as f:
            json.dump(data, f, indent=4)

config = ConfigLoader()