import json
import os
from typing import Any, Dict


class GameConfig(dict):
    """Dynamic game configuration mapping with preset fallback cascading and attribute access."""

    DEFAULTS: Dict[str, Any] = {
        "target_fps": 144,
        "render_scale": 1.0,
        "vsync": False,
        "max_frame_latency": 2,
        "fov": 103.0,
        "shadow_quality": "medium",
        "dlss_enabled": True,
        "thread_pool_size": 8,
    }

    PROFILES: Dict[str, Dict[str, Any]] = {
        "esports": {"target_fps": 240, "render_scale": 0.85, "shadow_quality": "low"},
        "cinematic": {"target_fps": 60, "render_scale": 1.0, "shadow_quality": "ultra"},
    }

    def __init__(self, profile: str = "custom", override_path: str = "game_config.json"):
        super().__init__()
        self.update(self.DEFAULTS)

        if profile in self.PROFILES:
            self.update(self.PROFILES[profile])

        if os.path.exists(override_path):
            try:
                with open(override_path, "r", encoding="utf-8") as f:
                    self.update(json.load(f))
            except (json.JSONDecodeError, OSError):
                pass

        for key, default_val in self.DEFAULTS.items():
            env_key = f"GAME_{key.upper()}"
            if env_key in os.environ:
                val = os.environ[env_key]
                self[key] = self._cast_value(val, type(default_val))

    @staticmethod
    def _cast_value(val: str, target_type: type) -> Any:
        if target_type is bool:
            return val.lower() in ("1", "true", "yes", "on")
        try:
            return target_type(val)
        except ValueError:
            return val

    def __getattr__(self, name: str) -> Any:
        try:
            return self[name]
        except KeyError:
            raise AttributeError(f"Configuration key '{name}' not found")

    def __setattr__(self, name: str, value: Any) -> None:
        self[name] = value


def load_config(profile: str = "esports") -> GameConfig:
    return GameConfig(profile=profile)
