from collections import deque
from typing import Dict, Generator
import math


class TelemetryStreamProcessor:
    """Creative pipeline for real-time game performance telemetry processing."""

    def __init__(self, buffer_size: int = 1000):
        self.buffer_size = buffer_size
        self._frame_times: deque[float] = deque(maxlen=buffer_size)
        self._gpu_temps: deque[float] = deque(maxlen=buffer_size)

    def push(self, frame_time_ms: float, gpu_temp: float) -> None:
        """Ingest a single frame metric into rolling buffers."""
        if frame_time_ms > 0:
            self._frame_times.append(frame_time_ms)
        if gpu_temp > 0:
            self._gpu_temps.append(gpu_temp)

    def calculate_percentiles(self) -> Dict[str, float]:
        """Compute average FPS, 1% low, 0.1% low, and thermal pressure penalty."""
        if not self._frame_times:
            return {"fps_avg": 0.0, "fps_low_1pct": 0.0, "fps_low_01pct": 0.0, "thermal_load": 0.0}

        sorted_ft = sorted(self._frame_times)
        count = len(sorted_ft)

        def _get_percentile_ft(pct: float) -> float:
            idx = math.ceil((pct / 100.0) * count) - 1
            return sorted_ft[max(0, min(idx, count - 1))]

        p99_ft = _get_percentile_ft(99.0)
        p999_ft = _get_percentile_ft(99.9)
        avg_ft = sum(self._frame_times) / count

        avg_fps = 1000.0 / avg_ft if avg_ft > 0 else 0.0
        low_1pct = 1000.0 / p99_ft if p99_ft > 0 else 0.0
        low_01pct = 1000.0 / p999_ft if p999_ft > 0 else 0.0

        avg_temp = sum(self._gpu_temps) / len(self._gpu_temps) if self._gpu_temps else 0.0
        thermal_load = max(0.0, min(100.0, (avg_temp - 50.0) * 2.5))

        return {
            "fps_avg": round(avg_fps, 2),
            "fps_low_1pct": round(low_1pct, 2),
            "fps_low_01pct": round(low_01pct, 2),
            "thermal_load": round(thermal_load, 1),
        }

    def frame_jitter_generator(self) -> Generator[float, None, None]:
        """Yield frame-to-frame delta fluctuations (stutter metric)."""
        ft_list = list(self._frame_times)
        for i in range(1, len(ft_list)):
            yield abs(ft_list[i] - ft_list[i - 1])
