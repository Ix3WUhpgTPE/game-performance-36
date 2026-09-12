import os
from dataclasses import dataclass
from typing import Final

@dataclass(frozen=True)
class EngineConfig:
    FPS_CAP: int = 144
    RENDER_SCALE: float = 1.0
    DEBUG_MODE: bool = False

class SettingsManager:
    _defaults: Final = EngineConfig()

    @classmethod
    def load_environment(cls) -> EngineConfig:
        try:
            return EngineConfig(
                FPS_CAP=int(os.getenv("GAME_FPS", cls._defaults.FPS_CAP)),
                RENDER_SCALE=float(os.getenv("GAME_SCALE", cls._defaults.RENDER_SCALE)),
                DEBUG_MODE=os.getenv("GAME_DEBUG", "0") == "1"
            )
        except (ValueError, TypeError):
            return cls._defaults

    @staticmethod
    def get_optimizations() -> dict:
        return {
            "texture_streaming": True,
            "shadow_lod": 2,
            "motion_blur": False
        }

active_config = SettingsManager.load_environment()