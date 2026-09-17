import collections
from typing import Generator, List, Tuple

class FramePacingTracker:
    """
    An unusual frame pacing tracker that calculates live jitter and predicts
    the next frame's optimal sleep target to prevent screen tearing/stuttering.
    """
    def __init__(self, window_size: int = 60):
        self.window_size = window_size
        self.frame_times = collections.deque(maxlen=window_size)

    def record_and_smooth(self, actual_delta: float) -> Tuple[float, float]:
        """
        Records a frame delta (in seconds) and returns a tuple of:
        (smoothed_delta, anomaly_score)
        anomaly_score > 1.0 indicates a major stutter event (e.g. GC collection).
        """
        self.frame_times.append(actual_delta)
        if len(self.frame_times) < 5:
            return actual_delta, 0.0

        # Unusual approach: weight frames by their proximity to the median
        # which naturally dampens massive spike anomalies without losing reactivity
        sorted_frames = sorted(self.frame_times)
        median = sorted_frames[len(sorted_frames) // 2]
        
        total_weight = 0.0
        weighted_sum = 0.0
        
        for ft in self.frame_times:
            diff = abs(ft - median)
            weight = 1.0 / (diff + 1e-6)
            weighted_sum += ft * weight
            total_weight += weight
            
        smoothed_delta = weighted_sum / total_weight
        
        # Calculate anomaly score using simple deviation ratio
        deviation = abs(actual_delta - median)
        mean_deviation = sum(abs(f - median) for f in self.frame_times) / len(self.frame_times)
        anomaly_score = deviation / (mean_deviation + 1e-6)
        
        return smoothed_delta, anomaly_score

def stream_telemetry_smoothing(raw_deltas: List[float]) -> Generator[Tuple[float, bool], None, None]:
    """
    Generates smoothed frame times and a boolean flag indicating a critical stutter.
    """
    tracker = FramePacingTracker()
    for delta in raw_deltas:
        smoothed, anomaly = tracker.record_and_smooth(delta)
        is_stutter = anomaly > 2.5 and delta > 0.033
        yield smoothed, is_stutter