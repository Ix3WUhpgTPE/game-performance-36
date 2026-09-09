import json
import os
from typing import Any, Dict

class ConfigLoader:
    def __init__(self, defaults: Dict[str, Any], path: str = 'settings.json'):
        self.path = path
        self.data = defaults
        self._load_from_disk()

    def _load_from_disk(self) -> None:
        if os.path.exists(self.path):
            try:
                with open(self.path, 'r') as f:
                    disk_data = json.load(f)
                    self.data.update(disk_data)
            except (json.JSONDecodeError, IOError):
                pass

    def __getattr__(self, name: str) -> Any:
        return self.data.get(name)

    def __getitem__(self, key: str) -> Any:
        return self.data[key]

    def save(self) -> None:
        with open(self.path, 'w') as f:
            json.dump(self.data, f, indent=4)

def get_config() -> ConfigLoader:
    defaults = {
        'fps_cap': 60,
        'vsync': True,
        'resolution': [1920, 1080],
        'audio_gain': 1.0
    }
    return ConfigLoader(defaults)