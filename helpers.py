from typing import List, Tuple, Callable
import math
import time


def frame_time_to_fps(frame_time_ms: float) -> float:
    """Convert frame time in milliseconds to frames per second."""
    return 1000.0 / max(frame_time_ms, 0.0001)


def calculate_percentile_fps(frame_times_ms: List[float], percentile: float) -> float:
    """Calculate percentile FPS (e.g., 99th percentile frame time for 1% low FPS)."""
    if not frame_times_ms:
        return 0.0
    sorted_times = sorted(frame_times_ms)
    idx = math.ceil((percentile / 100.0) * len(sorted_times)) - 1
    target_ms = sorted_times[min(max(idx, 0), len(sorted_times) - 1)]
    return frame_time_to_fps(target_ms)


def calculate_stutter_index(frame_times_ms: List[float], threshold_factor: float = 1.5) -> float:
    """Calculate stutter index percentage based on frame spike frequency."""
    if len(frame_times_ms) < 2:
        return 0.0
    
    avg_ms = sum(frame_times_ms) / len(frame_times_ms)
    stutters = sum(1 for ft in frame_times_ms if ft > avg_ms * threshold_factor)
    return round((stutters / len(frame_times_ms)) * 100, 2)


def benchmark_execution(fn: Callable, *args, **kwargs) -> Tuple[any, float]:
    """Execute target function and return tuple of (result, execution_time_ms)."""
    start = time.perf_counter()
    res = fn(*args, **kwargs)
    elapsed_ms = (time.perf_counter() - start) * 1000.0
    return res, round(elapsed_ms, 3)


def format_vram(bytes_val: int) -> str:
    """Format raw byte counts into human-readable VRAM strings."""
    units = ['B', 'KB', 'MB', 'GB', 'TB']
    val = float(bytes_val)
    unit_idx = 0
    while val >= 1024.0 and unit_idx < len(units) - 1:
        val /= 1024.0
        unit_idx += 1
    return f"{val:.2f} {units[unit_idx]}"
