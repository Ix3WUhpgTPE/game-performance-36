import math
import statistics
from collections import deque
from typing import List, Tuple, Callable, Dict, Any


class FrameBuffer:
    """Telemetry ring buffer supporting pipe-like evaluation syntax."""
    def __init__(self, capacity: int = 120):
        self._samples = deque(maxlen=capacity)

    def push(self, frametime_ms: float) -> "FrameBuffer":
        self._samples.append(max(0.1, frametime_ms))
        return self

    def __rshift__(self, operator: Callable[["FrameBuffer"], Any]) -> Any:
        return operator(self)


def extract_fps_metrics(buffer: FrameBuffer) -> Dict[str, Any]:
    """Pipeline operator: computes FPS statistics and micro-stutter frequencies."""
    if not buffer._samples:
        return {"avg_fps": 0.0, "p99_low_fps": 0.0, "stutter_count": 0}

    times = list(buffer._samples)
    fps_list = [1000.0 / t for t in times]
    sorted_fps = sorted(fps_list)
    
    p1_index = max(0, int(len(sorted_fps) * 0.01))
    avg_ft = statistics.mean(times)
    stutters = sum(1 for t in times if t > avg_ft * 2.5)

    return {
        "avg_fps": round(statistics.mean(fps_list), 1),
        "p99_low_fps": round(sorted_fps[p1_index], 1),
        "stutter_count": stutters,
    }


def smooth_hardware_load(gpu_loads: List[float], alpha: float = 0.3) -> List[float]:
    """Exponential moving average filter for volatile GPU metric streams."""
    if not gpu_loads:
        return []
    smoothed = [gpu_loads[0]]
    for val in gpu_loads[1:]:
        smoothed.append(round(alpha * val + (1 - alpha) * smoothed[-1], 2))
    return smoothed


def synthesize_frame_budget(target_fps: int = 60) -> Tuple[float, Callable[[float], bool]]:
    """Returns target frame budget threshold (ms) and a validator closure."""
    budget_ms = 1000.0 / max(1, target_fps)
    return budget_ms, lambda elapsed_ms: elapsed_ms <= budget_ms
