import json
import os
from typing import Any, Dict

class GameConfig:
    DEFAULT_SETTINGS = {
        "resolution": [1920, 1080],
        "vsync": True,
        "max_fps": 144,
        "texture_quality": "ultra"
    }

    def __init__(self, filepath: str = "settings.json"):
        self.filepath = filepath
        self.settings = self._load_or_create()

    def _load_or_create(self) -> Dict[str, Any]:
        if not os.path.exists(self.filepath):
            with open(self.filepath, "w") as f:
                json.dump(self.DEFAULT_SETTINGS, f, indent=4)
            return self.DEFAULT_SETTINGS.copy()
        
        with open(self.filepath, "r") as f:
            data = json.load(f)
            return {**self.DEFAULT_SETTINGS, **data}

    def get(self, key: str, fallback: Any = None) -> Any:
        return self.settings.get(key, fallback)

    def set(self, key: str, value: Any) -> None:
        self.settings[key] = value
        with open(self.filepath, "w") as f:
            json.dump(self.settings, f, indent=4)

    def __getitem__(self, item: str) -> Any:
        return self.settings[item]

    def __repr__(self) -> str:
        return f"GameConfig({self.settings})"