import json
import os
from typing import Any, Dict

class GameConfig:
    DEFAULT_SETTINGS = {
        "frame_rate_cap": 144,
        "vsync": True,
        "resolution": [1920, 1080],
        "debug_mode": False
    }

    def __init__(self, path: str = "settings.json"):
        self.path = path
        self.data = self._load()

    def _load(self) -> Dict[str, Any]:
        if not os.path.exists(self.path):
            self._save(self.DEFAULT_SETTINGS)
            return self.DEFAULT_SETTINGS.copy()
        
        try:
            with open(self.path, "r") as f:
                loaded = json.load(f)
                return {**self.DEFAULT_SETTINGS, **loaded}
        except (json.JSONDecodeError, IOError):
            return self.DEFAULT_SETTINGS.copy()

    def _save(self, data: Dict[str, Any]) -> None:
        with open(self.path, "w") as f:
            json.dump(data, f, indent=4)

    def get(self, key: str, default: Any = None) -> Any:
        return self.data.get(key, default)

    def __getitem__(self, key: str) -> Any:
        return self.data[key]

    def __repr__(self) -> str:
        return f"<GameConfig path={self.path} keys={list(self.data.keys())}>"