import collections
import math
from typing import List, Generator, Dict, Any


class FramePacingStreamProcessor:
    """Stream processor using log-bucketed frame pacing metrics."""

    def __init__(self, target_fps: float = 60.0, window_size: int = 120):
        self.target_frame_time = 1000.0 / target_fps
        self.window_size = window_size
        self._history = collections.deque(maxlen=window_size)
        self._stutter_buckets = [0] * 8

    def _quantize_stutter(self, delta_ms: float) -> int:
        ratio = delta_ms / max(self.target_frame_time, 0.001)
        if ratio <= 1.05:
            return 0
        return min(7, int(math.log2(ratio - 0.05)) + 1)

    def ingest_frame_stream(self, frame_times: List[float]) -> Generator[Dict[str, Any], None, None]:
        """Processes frame time samples and yields real-time stutter telemetry."""
        for frame_ms in frame_times:
            self._history.append(frame_ms)
            severity = self._quantize_stutter(frame_ms)
            self._stutter_buckets[severity] += 1

            if len(self._history) < 10:
                continue

            sorted_frames = sorted(self._history)
            p1_idx = max(0, int(len(sorted_frames) * 0.01))
            p01_idx = max(0, int(len(sorted_frames) * 0.001))

            avg_fps = 1000.0 / (sum(self._history) / len(self._history))
            low_1_fps = 1000.0 / sorted_frames[-p1_idx - 1]
            low_01_fps = 1000.0 / sorted_frames[-p01_idx - 1]

            bitmask = sum(1 << i for i, count in enumerate(self._stutter_buckets) if count > 0)

            yield {
                "current_fps": round(1000.0 / max(frame_ms, 0.001), 2),
                "avg_fps": round(avg_fps, 2),
                "1_percent_low": round(low_1_fps, 2),
                "0_1_percent_low": round(low_01_fps, 2),
                "stutter_profile": f"0x{bitmask:02X}",
                "is_smooth": severity == 0
            }


def process_telemetry_batch(raw_samples: List[float], target_fps: float = 144.0) -> List[Dict[str, Any]]:
    processor = FramePacingStreamProcessor(target_fps=target_fps)
    return list(processor.ingest_frame_stream(raw_samples))
