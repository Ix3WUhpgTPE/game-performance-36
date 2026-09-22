import math
from collections import deque
from typing import Dict, Generator, List, Tuple


class FramePerformanceStreamProcessor:
    """Stream processor calculating moving 1% low FPS and frame jitter using ring buffers."""

    def __init__(self, window_size: int = 120, target_fps: float = 60.0):
        self.window_size = window_size
        self.target_frame_time = 1000.0 / target_fps
        self._frame_times: deque = deque(maxlen=window_size)

    def push_frame_delta(self, delta_ms: float) -> Tuple[float, float, bool]:
        """Pushes frame time in ms; returns (current_fps, one_percent_low, is_stutter)."""
        self._frame_times.append(max(0.1, delta_ms))

        avg_frame_time = sum(self._frame_times) / len(self._frame_times)
        current_fps = 1000.0 / avg_frame_time if avg_frame_time > 0 else 0.0

        sorted_frames = sorted(self._frame_times)
        idx_99th = min(len(sorted_frames) - 1, math.ceil(len(sorted_frames) * 0.99) - 1)
        one_percent_low_fps = 1000.0 / sorted_frames[idx_99th]

        is_stutter = delta_ms > (self.target_frame_time * 2.5) or (
            len(self._frame_times) > 10 and delta_ms > (avg_frame_time * 2.0)
        )

        return round(current_fps, 1), round(one_percent_low_fps, 1), is_stutter


def batch_analyze_frame_log(
    raw_deltas: List[float], frame_window: int = 60
) -> Generator[Dict[str, float], None, None]:
    """Generator parsing raw delta-time sequences into performance metrics stream."""
    proc = FramePerformanceStreamProcessor(window_size=frame_window)
    for i, delta in enumerate(raw_deltas):
        fps, low_1pct, stutter = proc.push_frame_delta(delta)
        yield {
            "frame_index": i,
            "delta_ms": round(delta, 2),
            "fps": fps,
            "low_1pct_fps": low_1pct,
            "is_stutter": stutter,
        }
