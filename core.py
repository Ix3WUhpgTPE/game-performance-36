import math
from typing import List, Dict, Union

class PerformanceEvaluator:
    """
    Analyzes raw game frame timestamps to evaluate frame pacing and micro-stuttering.
    Uses an entropy-based consistency metric rather than simple standard deviation.
    """
    def __init__(self, target_fps: int = 60):
        self.target_frame_time = 1000.0 / target_fps

    def analyze_pacing(self, timestamps_ms: List[float]) -> Dict[str, Union[float, str]]:
        if len(timestamps_ms) < 2:
            return {"smoothness_index": 1.0, "status": "insufficient_data", "entropy": 0.0}

        frame_times = [
            timestamps_ms[i] - timestamps_ms[i - 1]
            for i in range(1, len(timestamps_ms))
        ]

        total_frames = len(frame_times)
        avg_frame_time = sum(frame_times) / total_frames

        bin_width = 2.0
        bins: Dict[int, int] = {}
        for ft in frame_times:
            deviation = ft - self.target_frame_time
            bin_idx = int(deviation // bin_width)
            bins[bin_idx] = bins.get(bin_idx, 0) + 1

        entropy = 0.0
        for count in bins.values():
            probability = count / total_frames
            entropy -= probability * math.log2(probability)

        max_tolerable_entropy = 3.32
        smoothness = max(0.0, 1.0 - (entropy / max_tolerable_entropy))

        if smoothness > 0.85:
            status = "fluid"
        elif smoothness > 0.60:
            status = "acceptable_micro_stutter"
        else:
            status = "unstable_pacing"

        return {
            "average_fps": round(1000.0 / avg_frame_time, 2) if avg_frame_time > 0 else 0.0,
            "smoothness_index": round(smoothness, 4),
            "entropy": round(entropy, 4),
            "status": status,
            "total_stutters": sum(1 for ft in frame_times if ft > self.target_frame_time * 1.5)
        }