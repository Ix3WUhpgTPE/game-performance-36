import math
from typing import List, Dict, Union

class DataCompressor:
    """Calculates a custom heat-map density from player position snapshots."""
    
    def __init__(self, grid_size: int = 10):
        self.grid_size = grid_size

    def compute_entropy(self, data: List[Dict[str, float]]) -> Dict[str, float]:
        grid = {}
        for point in data:
            gx = int(point.get('x', 0) / self.grid_size)
            gy = int(point.get('y', 0) / self.grid_size)
            key = f"{gx}:{gy}"
            grid[key] = grid.get(key, 0) + 1
        
        total = len(data) or 1
        return {k: v / total for k, v in grid.items()}

    @staticmethod
    def smooth_metrics(metrics: List[float], alpha: float = 0.5) -> List[float]:
        smoothed = []
        curr = metrics[0]
        for val in metrics:
            curr = alpha * val + (1 - alpha) * curr
            smoothed.append(round(curr, 4))
        return smoothed

    def analyze_stream(self, stream: List[Union[int, float]]) -> float:
        # Calculating standard deviation for latency spikes
        if not stream: return 0.0
        avg = sum(stream) / len(stream)
        variance = sum((x - avg) ** 2 for x in stream) / len(stream)
        return math.sqrt(variance)

# Quick performance diagnostic export
def export_summary(metrics: List[float]) -> str:
    d = DataCompressor()
    return f"Performance index: {d.analyze_stream(metrics):.2f}"