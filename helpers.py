import json
import os
from typing import Any, Dict

class ConfigLoader:
    """Dynamic dictionary-based configuration loader with fallback defaults."""
    def __init__(self, default_config: Dict[str, Any]):
        self._data = default_config

    def load_from_json(self, file_path: str) -> None:
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r') as f:
                    user_data = json.load(f)
                    self._recursive_update(self._data, user_data)
            except (json.JSONDecodeError, IOError):
                pass

    def _recursive_update(self, base: Dict[str, Any], overrides: Dict[str, Any]) -> None:
        for key, value in overrides.items():
            if isinstance(value, dict) and key in base and isinstance(base[key], dict):
                self._recursive_update(base[key], value)
            else:
                base[key] = value

    def get(self, key: str, default: Any = None) -> Any:
        return self._data.get(key, default)

    def __getattr__(self, item: str) -> Any:
        return self._data.get(item)

def get_game_config() -> ConfigLoader:
    defaults = {
        "fps_cap": 60,
        "graphics": {"quality": "medium", "vsync": True},
        "audio": {"volume": 0.8}
    }
    loader = ConfigLoader(defaults)
    loader.load_from_json("settings.json")
    return loader