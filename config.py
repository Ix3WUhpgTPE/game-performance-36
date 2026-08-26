import json
import os
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "resolution": [1920, 1080],
    "vsync": True,
    "target_fps": 144,
    "shader_quality": "ultra"
}

class GameConfig:
    def __init__(self, config_path: str = "settings.json") -> None:
        self.path = config_path
        self.settings = self._load_and_merge()

    def _load_and_merge(self) -> Dict[str, Any]:
        config = DEFAULT_CONFIG.copy()
        if os.path.exists(self.path):
            try:
                with open(self.path, "r", encoding="utf-8") as f:
                    user_data = json.load(f)
                    config.update({k: v for k, v in user_data.items() if k in config})
            except (json.JSONDecodeError, IOError):
                pass
        return config

    def __getattr__(self, name: str) -> Any:
        if name in self.settings:
            return self.settings[name]
        raise AttributeError(f"'GameConfig' object has no attribute '{name}'")

    def save(self) -> None:
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(self.settings, f, indent=4)

config = GameConfig()
