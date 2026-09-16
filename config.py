import os
from contextlib import contextmanager
from typing import Any, Dict, get_type_hints


class GameConfig:
    # Game performance default settings
    TARGET_FPS: int = 144
    ENABLE_V_SYNC: bool = False
    GC_GENERATION_LIMIT: int = 3
    RENDER_SCALE: float = 1.0
    SHADOW_RESOLUTION: int = 1024
    CACHE_SIZE_MB: int = 512
    LOG_PERFORMANCE_METRICS: bool = True

    def __init__(self, overrides: Dict[str, Any] = None):
        self._custom = overrides or {}
        self._temp_overrides = {}

    def _coerce(self, name: str, value: Any) -> Any:
        hints = get_type_hints(self.__class__)
        if name not in hints:
            return value
        expected_type = hints[name]
        if isinstance(value, expected_type):
            return value
        if expected_type is bool:
            return str(value).lower() in ("true", "1", "yes", "on")
        try:
            return expected_type(value)
        except (ValueError, TypeError):
            return getattr(self.__class__, name)

    def __getattr__(self, name: str) -> Any:
        if name.startswith("_"):
            raise AttributeError(
                f"'{self.__class__.__name__}' object has no attribute '{name}'"
            )

        # Priority: Temp override > Environment > Custom Overrides > Class Defaults
        if name in self._temp_overrides:
            return self._coerce(name, self._temp_overrides[name])

        env_val = os.environ.get(f"GAME_{name.upper()}")
        if env_val is not None:
            return self._coerce(name, env_val)

        if name in self._custom:
            return self._coerce(name, self._custom[name])

        if hasattr(self.__class__, name):
            return getattr(self.__class__, name)

        raise AttributeError(
            f"Config option '{name}' is not defined in defaults."
        )

    @contextmanager
    def override(self, **kwargs):
        """Temporary performance tuning context helper."""
        old_overrides = dict(self._temp_overrides)
        self._temp_overrides.update(kwargs)
        try:
            yield self
        finally:
            self._temp_overrides = old_overrides
