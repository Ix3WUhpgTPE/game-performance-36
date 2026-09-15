from typing import Dict, List, Any, Optional

class FrameDeltaHandler:
    """Calculates performance variance between frames for gaming telemetry."""

    def __init__(self, target_fps: int = 60) -> None:
        self.frame_time: float = 1.0 / target_fps
        self.history: List[float] = []

    def process_delta(self, actual_delta: float) -> Dict[str, Any]:
        """Analyzes time deviation and returns status payload."""
        variance: float = actual_delta - self.frame_time
        is_laggy: bool = variance > 0.005
        
        self.history.append(actual_delta)
        if len(self.history) > 100:
            self.history.pop(0)
            
        return {
            "jitter": round(variance, 6),
            "dropped_frame": is_laggy,
            "load_score": self._calculate_pressure()
        }

    def _calculate_pressure(self) -> float:
        """Heuristic for system thermal or processing bottleneck."""
        if not self.history:
            return 0.0
        avg: float = sum(self.history) / len(self.history)
        return min(1.0, avg / self.frame_time)

    def reset_metrics(self) -> None:
        """Clears frame history buffer."""
        self.history = []