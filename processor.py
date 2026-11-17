from typing import List, Dict, Union, Callable

class FrameProcessor:
    """Advanced heuristic processor for game engine frame timings."""

    def __init__(self, target_fps: int = 60) -> None:
        self.target_frame_time: float = 1.0 / target_fps
        self.history: List[float] = []

    def ingest_frame(self, delta: float) -> bool:
        """Check if frame delta exceeds target budget."""
        self.history.append(delta)
        return delta > self.target_frame_time

    def get_performance_metric(self, strategy: Callable[[List[float]], float]) -> float:
        """Execute custom analysis strategy on recorded frame data."""
        if not self.history:
            return 0.0
        return strategy(self.history)

def compute_jank_factor(data: List[float]) -> float:
    """Calculate variance coefficient to detect frame stuttering."""
    mean_val: float = sum(data) / len(data)
    variance: float = sum((x - mean_val) ** 2 for x in data) / len(data)
    return variance ** 0.5

def run_pipeline(frame_deltas: List[float]) -> Dict[str, Union[float, bool]]:
    """Orchestrate processing of engine telemetry data."""
    processor = FrameProcessor()
    critical_frames: int = sum(1 for d in frame_deltas if processor.ingest_frame(d))
    
    return {
        "jank": compute_jank_factor(frame_deltas),
        "has_stutter": critical_frames > (len(frame_deltas) * 0.05)
    }