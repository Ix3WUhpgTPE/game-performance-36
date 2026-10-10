import json
import os
from collections import ChainMap
from pathlib import Path
from typing import Any, Dict, Union

DEFAULT_PROFILE: Dict[str, Any] = {
    "target_fps": 144,
    "overlay_enabled": True,
    "overlay_position": "top_left",
    "telemetry_interval_ms": 250,
    "auto_adjust_resolution": False,
    "gpu_power_plan": "ultra_performance",
    "hotkeys": {"toggle_overlay": "F11", "benchmark": "F12"},
}

class GamingConfig(ChainMap):
    """Cascading configuration layer for gaming overlay and performance tuning."""

    def __init__(self, config_path: Union[str, Path] = "game_perf.json", **overrides):
        file_cfg = self._load_json(Path(config_path))
        env_cfg = self._extract_env_overrides()
        super().__init__(overrides, env_cfg, file_cfg, DEFAULT_PROFILE)

    def _load_json(self, path: Path) -> Dict[str, Any]:
        if path.exists() and path.is_file():
            try:
                with path.open("r", encoding="utf-8") as f:
                    return json.load(f)
            except json.JSONDecodeError:
                pass
        return {}

    def _extract_env_overrides(self) -> Dict[str, Any]:
        env_map = {}
        prefix = "GAME_PERF_"
        for key, val in os.environ.items():
            if key.startswith(prefix):
                clean_key = key[len(prefix):].lower()
                if val.isdigit():
                    env_map[clean_key] = int(val)
                elif val.lower() in ("true", "false"):
                    env_map[clean_key] = val.lower() == "true"
                else:
                    env_map[clean_key] = val
        return env_map

    def __getattr__(self, item: str) -> Any:
        try:
            return self[item]
        except KeyError:
            raise AttributeError(f"Configuration key '{item}' not found")

    def export_flat(self) -> Dict[str, Any]:
        return dict(self)
