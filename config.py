import json
import os
from collections import ChainMap
from typing import Any, Dict

DEFAULT_GAME_SETTINGS: Dict[str, Any] = {
    "target_fps": 60,
    "resolution_scale": 1.0,
    "max_frame_latency": 2,
    "v_sync": True,
    "texture_pool_mb": 2048,
    "enable_hud_overlay": False,
    "shadow_quality": "medium",
    "preset": "balanced",
}

PRESETS: Dict[str, Dict[str, Any]] = {
    "esports": {
        "target_fps": 144,
        "resolution_scale": 0.85,
        "shadow_quality": "low",
        "v_sync": False,
    },
    "ultra": {
        "target_fps": 60,
        "resolution_scale": 1.0,
        "shadow_quality": "ultra",
        "texture_pool_mb": 4096,
    },
    "power_saver": {
        "target_fps": 30,
        "resolution_scale": 0.75,
        "shadow_quality": "low",
        "v_sync": True,
    },
}


class DynamicConfigLoader:
    """Loads engine performance settings with fallback cascades and presets."""

    def __init__(self, config_path: str = "settings.json"):
        self.config_path = config_path
        self._runtime_overrides: Dict[str, Any] = {}
        self.settings = ChainMap(
            self._runtime_overrides,
            self._load_file(),
            DEFAULT_GAME_SETTINGS,
        )

    def _load_file(self) -> Dict[str, Any]:
        if os.path.exists(self.config_path):
            try:
                with open(self.config_path, "r", encoding="utf-8") as f:
                    return json.load(f)
            except (json.JSONDecodeError, OSError):
                pass
        return {}

    def apply_preset(self, name: str) -> None:
        if name in PRESETS:
            self._runtime_overrides.clear()
            self._runtime_overrides.update(PRESETS[name])
            self._runtime_overrides["preset"] = name

    def override(self, key: str, value: Any) -> None:
        self._runtime_overrides[key] = value

    def __getattr__(self, name: str) -> Any:
        if name in self.settings:
            return self.settings[name]
        raise AttributeError(f"Configuration key '{name}' does not exist.")

    def __getitem__(self, item: str) -> Any:
        return self.settings[item]

    def dump_active(self) -> Dict[str, Any]:
        return dict(self.settings)
