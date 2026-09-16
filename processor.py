import math
from collections import deque
from typing import Dict, Iterable, List

class PerformanceTelemetryProcessor:
    """Filters, aggregates, and processes raw game frame times with anomaly suppression."""
    
    def __init__(self, max_samples: int = 2000, anomaly_threshold_ms: float = 500.0):
        self._samples: deque = deque(maxlen=max_samples)
        self.anomaly_threshold_ms = anomaly_threshold_ms

    def ingest_telemetry(self, frame_times: Iterable[float]) -> int:
        """Cleans out dead/anomaly frames (loading screens, alt-tabs) and ingests the rest."""
        valid_count = 0
        for ft in frame_times:
            if 0.1 <= ft < self.anomaly_threshold_ms:
                self._samples.append(ft)
                valid_count += 1
        return valid_count

    def compute_performance_profile(self) -> Dict[str, float]:
        """Calculates key gaming performance indices including average and low-percentile FPS."""
        if not self._samples:
            return {"fps_avg": 0.0, "fps_low_1pct": 0.0, "fps_low_01pct": 0.0, "jitter_ms": 0.0}

        sorted_frames = sorted(list(self._samples))
        total = len(sorted_frames)
        
        avg_ft = sum(sorted_frames) / total
        fps_avg = 1000.0 / avg_ft if avg_ft > 0 else 0.0

        # Calculate average of the slowest 1% and 0.1% of frames
        count_1pct = max(1, int(total * 0.01))
        count_01pct = max(1, int(total * 0.001))

        slow_1pct_avg = sum(sorted_frames[-count_1pct:]) / count_1pct
        slow_01pct_avg = sum(sorted_frames[-count_01pct:]) / count_01pct

        # Jitter calculation (mean absolute difference between consecutive frames)
        raw_list = list(self._samples)
        jitter = (
            sum(abs(raw_list[i] - raw_list[i - 1]) for i in range(1, len(raw_list)))
            / (len(raw_list) - 1) if len(raw_list) > 1 else 0.0
        )

        return {
            "fps_avg": round(fps_avg, 2),
            "fps_low_1pct": round(1000.0 / slow_1pct_avg, 2) if slow_1pct_avg > 0 else 0.0,
            "fps_low_01pct": round(1000.0 / slow_01pct_avg, 2) if slow_01pct_avg > 0 else 0.0,
            "jitter_ms": round(jitter, 4)
        }

    def clear(self) -> None:
        self._samples.clear()