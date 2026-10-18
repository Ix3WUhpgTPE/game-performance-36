from typing import Dict, List, Union, Optional

class FrameBatchHandler:
    """Handles high-frequency frame data for performance metrics."""

    def __init__(self, buffer_size: int = 60) -> None:
        self.buffer: List[float] = []
        self.buffer_size: int = buffer_size

    def ingest_frame_time(self, delta_time: float) -> Optional[float]:
        """Adds a new frame duration and returns current average."""
        self.buffer.append(delta_time)
        if len(self.buffer) > self.buffer_size:
            self.buffer.pop(0)
        return sum(self.buffer) / len(self.buffer)

    def get_performance_stats(self) -> Dict[str, Union[int, float]]:
        """Calculates basic performance snapshot for the frame buffer."""
        if not self.buffer:
            return {"avg": 0.0, "count": 0}
        
        avg_dt: float = sum(self.buffer) / len(self.buffer)
        return {
            "avg": round(avg_dt, 4),
            "fps_estimate": round(1.0 / avg_dt, 2) if avg_dt > 0 else 0.0,
            "count": len(self.buffer)
        }

def process_batch(data: List[float], handler: FrameBatchHandler) -> Dict[str, float]:
    """Batch processing utility for frame timing inputs."""
    for entry in data:
        handler.ingest_frame_time(entry)
    return handler.get_performance_stats()