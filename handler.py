from typing import Dict, List, Any, Union, Optional

class GamePerformanceHandler:
    """Manages frame latency and telemetry snapshots for game-performance-36."""

    def __init__(self, target_fps: int = 60) -> None:
        self.target_fps: float = float(target_fps)
        self.telemetry: Dict[str, List[float]] = {"frame_times": []}

    def ingest_frame_data(self, delta_time: float) -> Optional[float]:
        """Calculates jitter variance using a rolling frame analysis approach."""
        self.telemetry["frame_times"].append(delta_time)
        if len(self.telemetry["frame_times"]) > 100:
            self.telemetry["frame_times"].pop(0)
        return self._evaluate_performance(delta_time)

    def _evaluate_performance(self, current_dt: float) -> float:
        """Determines performance health score based on target deviation."""
        ideal: float = 1.0 / self.target_fps
        return max(0.0, 1.0 - abs(current_dt - ideal) / ideal)

    def get_summary(self) -> Dict[str, Union[float, int]]:
        """Generates snapshot report for performance tuning utilities."""
        times: List[float] = self.telemetry["frame_times"]
        avg_dt: float = sum(times) / len(times) if times else 0.0
        return {
            "avg_ms": round(avg_dt * 1000, 2),
            "sample_size": len(times),
            "status": "optimal" if avg_dt <= (1.0 / self.target_fps) else "degraded"
        }