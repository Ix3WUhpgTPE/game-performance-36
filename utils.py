import statistics
from collections import deque
from typing import Dict, List, Tuple, Union

class FrameMetricsProcessor:
    """
    Processes frame timing telemetry and detects micro-stutters
    using dynamic quantile analysis over a rolling ring buffer.
    """
    STUTTER_BIT = 1 << 0
    SPIKE_BIT = 1 << 1

    def __init__(self, capacity: int = 120):
        self._buffer = deque(maxlen=capacity)
        self._flag_history = deque(maxlen=capacity)

    def ingest_frame_time(self, frame_ms: float) -> int:
        """Pushes frame time in ms, returns bitwise status flags."""
        flags = 0
        if self._buffer:
            avg = statistics.fmean(self._buffer)
            if frame_ms > avg * 2.5:
                flags |= self.SPIKE_BIT
            if frame_ms > avg * 1.5:
                flags |= self.STUTTER_BIT

        self._buffer.append(frame_ms)
        self._flag_history.append(flags)
        return flags

    def summarize_performance(self) -> Dict[str, Union[float, Dict[str, float]]]:
        if not self._buffer:
            return {"fps_avg": 0.0, "p99_ms": 0.0, "stutter_rate": 0.0}

        fps_values = [1000.0 / ms for ms in self._buffer if ms > 0]
        sorted_ms = sorted(self._buffer)
        p99_index = min(int(len(sorted_ms) * 0.99), len(sorted_ms) - 1)
        stutters = sum(1 for f in self._flag_history if f & self.STUTTER_BIT)

        return {
            "fps_avg": round(statistics.fmean(fps_values), 2) if fps_values else 0.0,
            "fps_min": round(min(fps_values), 2) if fps_values else 0.0,
            "p99_ms": round(sorted_ms[p99_index], 2),
            "stutter_rate": round(stutters / len(self._flag_history), 4)
        }


def process_telemetry_stream(raw_samples: List[float], buffer_size: int = 60) -> Tuple[Dict[str, float], List[int]]:
    """Utility function to process frame samples and yield summary stats."""
    processor = FrameMetricsProcessor(capacity=buffer_size)
    flag_log = [processor.ingest_frame_time(sample) for sample in raw_samples]
    return processor.summarize_performance(), flag_log
