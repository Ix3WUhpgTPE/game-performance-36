import json
import os
from typing import Any, Dict

def load_game_config(path: str = "config.json") -> Dict[str, Any]:
    """Dynamic config loader with fallback defaults."""
    defaults = {
        "resolution": [1920, 1080],
        "vsync": True,
        "target_fps": 144,
        "shader_cache_size": 1024
    }

    if not os.path.exists(path):
        return defaults

    try:
        with open(path, 'r') as f:
            user_config = json.load(f)
    except (json.JSONDecodeError, IOError):
        return defaults

    return {**defaults, **{k: v for k, v in user_config.items() if k in defaults}}

def save_game_config(config: Dict[str, Any], path: str = "config.json") -> bool:
    """Persists game state settings to disk."""
    try:
        with open(path, 'w') as f:
            json.dump(config, f, indent=4)
        return True
    except IOError:
        return False

# Quick access factory pattern
class ConfigStore:
    def __init__(self, path: str = "config.json"):
        self.path = path
        self.data = load_game_config(path)

    def get(self, key: str, default: Any = None) -> Any:
        return self.data.get(key, default)

    def sync(self) -> None:
        save_game_config(self.data, self.path)