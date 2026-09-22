import json
import os
from pathlib import Path
from typing import Any, Dict, Union

DEFAULT_CONFIG: Dict[str, Any] = {
    "target_fps": 144,
    "overlay": {
        "enabled": True,
        "opacity": 0.85,
        "position": "top_right",
        "refresh_rate_ms": 100,
    },
    "metrics": {
        "track_gpu_temp": True,
        "track_vram_usage": True,
        "sample_interval_sec": 0.5,
    },
    "log_level": "INFO",
}


class ConfigProxy:
    """Dynamic cascading configuration structure with attribute access and env overrides."""

    def __init__(self, data: Dict[str, Any] | None = None, prefix: str = "GP36"):
        self._prefix = prefix
        self._data = data if data is not None else {}

    def __getattr__(self, item: str) -> Any:
        if item in self._data:
            val = self._data[item]
            if isinstance(val, dict):
                return ConfigProxy(val, prefix=f"{self._prefix}_{item.upper()}")
            return val

        env_key = f"{self._prefix}_{item.upper()}"
        if env_key in os.environ:
            return self._parse_env(os.environ[env_key])

        raise AttributeError(f"Configuration key '{item}' not found in cascade")

    def __getitem__(self, item: str) -> Any:
        return getattr(self, item)

    def _parse_env(self, val: str) -> Union[int, float, bool, str]:
        if val.lower() in ("true", "false"):
            return val.lower() == "true"
        try:
            return int(val)
        except ValueError:
            try:
                return float(val)
            except ValueError:
                return val

    def get(self, item: str, default: Any = None) -> Any:
        try:
            return getattr(self, item)
        except AttributeError:
            return default


def load_config(path: Union[str, Path, None] = None) -> ConfigProxy:
    merged = json.loads(json.dumps(DEFAULT_CONFIG))
    if path and Path(path).exists():
        with open(path, "r", encoding="utf-8") as f:
            user_data = json.load(f)
            merged = _deep_merge(merged, user_data)
    return ConfigProxy(merged)


def _deep_merge(base: dict, override: dict) -> dict:
    res = base.copy()
    for k, v in override.items():
        if k in res and isinstance(res[k], dict) and isinstance(v, dict):
            res[k] = _deep_merge(res[k], v)
        else:
            res[k] = v
    return res
