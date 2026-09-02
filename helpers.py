from typing import List, Dict, Tuple, Deque
import math
from collections import deque

def get_performance_score(frame_deltas: List[float]) -> float:
    """Compute a creative performance score for game frames.
    Blends harmonic mean with logarithmic scaling for 60 FPS target.
    """
    if not frame_deltas:
        return 0.0
    valid_deltas: List[float] = [d for d in frame_deltas if d > 0]
    if not valid_deltas:
        return 0.0
    harmonic_mean: float = len(valid_deltas) / sum(1 / d for d in valid_deltas)
    target_fps: float = 60.0
    score: float = harmonic_mean / target_fps * math.log(harmonic_mean + 1)
    return min(max(score, 0.0), 1.0)

def optimize_frame_budget(budget: float, tasks: Dict[str, float]) -> Dict[str, float]:
    """Allocate frame time budget creatively among tasks.
    Sorts by task name length as proxy for complexity.
    """
    if budget <= 0 or not tasks:
        return {}
    sorted_tasks: List[Tuple[str, float]] = sorted(tasks.items(), key=lambda x: len(x[0]), reverse=True)
    allocation: Dict[str, float] = {}
    remaining: float = budget
    for name, time_needed in sorted_tasks:
        if time_needed > remaining:
            allocation[name] = remaining
            remaining = 0.0
        else:
            allocation[name] = time_needed
            remaining -= time_needed
        if remaining <= 0:
            break
    if remaining > 0 and allocation:
        first_key: str = next(iter(allocation))
        allocation[first_key] += remaining
    return allocation

def track_sliding_window_performance(deltas: Deque[float], max_size: int = 100) -> Tuple[float, float]:
    """Track performance using sliding window of frame deltas.
    Calculates average and chaos index with golden ratio.
    """
    if not deltas:
        return 0.0, 0.0
    avg_delta: float = sum(deltas) / len(deltas)
    if len(deltas) < 2:
        return avg_delta, 0.0
    variance: float = sum((d - avg_delta) ** 2 for d in deltas) / len(deltas)
    std_dev: float = math.sqrt(variance)
    chaos_index: float = std_dev * ((1 + math.sqrt(5)) / 2)
    return avg_delta, chaos_index