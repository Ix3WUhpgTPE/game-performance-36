import time
import math
from typing import List, Optional

class TelemetryError(Exception):
    """Base exception for telemetry glitches."""
    pass

class PerformanceTracker:
    def __init__(self, target_fps: float = 60.0):
        self.target_fps = target_fps
        self.frame_times: List[float] = []
        self._last_tick: Optional[float] = None

    def tick(self, current_time: float) -> float:
        if self._last_tick is None:
            self._last_tick = current_time
            return 1.0 / self.target_fps

        dt = current_time - self._last_tick
        
        # Edge case 1: Time travelled backwards (NTP sync / timer glitch)
        if dt < 0:
            recent = self.frame_times[-10:]
            dt = sum(recent) / max(len(recent), 1) if recent else (1.0 / self.target_fps)
        
        # Edge case 2: Extreme lag spike (clamp freeze duration)
        elif dt > 5.0:
            dt = 5.0
            
        # Edge case 3: Zero delta precision limit
        elif math.isclose(dt, 0.0):
            dt = 1e-6

        self._last_tick = current_time
        self.frame_times.append(dt)
        if len(self.frame_times) > 1000:
            self.frame_times.pop(0)
            
        return dt

    def calculate_fps(self) -> float:
        try:
            recent = self.frame_times[-60:]
            if not recent:
                return self.target_fps
            avg_dt = sum(recent) / len(recent)
            return 1.0 / avg_dt
        except (ZeroDivisionError, OverflowError):
            return self.target_fps
