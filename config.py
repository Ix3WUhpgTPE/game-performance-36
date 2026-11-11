import os
import json
from typing import Any, Dict, Optional

DEFAULT_PROFILES: Dict[str, Dict[str, Any]] = {
    "ultra": {"target_fps": 144, "resolution_scale": 1.0, "vsync": False, "shadow_quality": "high", "thread_affinity": [0, 1, 2, 3]},
    "balanced": {"target_fps": 60, "resolution_scale": 0.85, "vsync": True, "shadow_quality": "medium", "thread_affinity": [0, 1]},
    "potato": {"target_fps": 30, "resolution_scale": 0.5, "vsync": False, "shadow_quality": "off", "thread_affinity": [0]},
}


class LazyConfigProxy:
    """Dynamic gaming performance configuration loader with fallback cascade."""

    def __init__(self, profile_name: str = "balanced", custom_path: Optional[str] = None):
        self._profile = profile_name
        self._defaults = DEFAULT_PROFILES.get(profile_name, DEFAULT_PROFILES["balanced"]).copy()
        self._loaded: Dict[str, Any] = {}
        if custom_path and os.path.exists(custom_path):
            with open(custom_path, "r", encoding="utf-8") as f:
                self._loaded = json.load(f)

    def __getattr__(self, item: str) -> Any:
        env_key = f"GAME_PERF_{item.upper()}"
        if env_key in os.environ:
            val = os.environ[env_key]
            try:
                return json.loads(val)
            except Exception:
                return val
        if item in self._loaded:
            return self._loaded[item]
        if item in self._defaults:
            return self._defaults[item]
        raise AttributeError(f"Configuration key '{item}' not found in profile '{self._profile}'")

    def __getitem__(self, item: str) -> Any:
        return getattr(self, item)

    def get(self, item: str, default: Any = None) -> Any:
        try:
            return getattr(self, item)
        except AttributeError:
            return default

    def export_active(self) -> Dict[str, Any]:
        merged = self._defaults.copy()
        merged.update(self._loaded)
        for k in list(merged.keys()):
            env_val = os.getenv(f"GAME_PERF_{k.upper()}")
            if env_val is not None:
                try:
                    merged[k] = json.loads(env_val)
                except Exception:
                    merged[k] = env_val
        return merged
