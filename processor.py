from typing import Generator, Iterable, TypeVar

T = TypeVar("T")

class FrameDeltaSmoother:
    """Exponential moving average smoother for frame delta time processing.
    
    Uses bitwise right shift operator overloading to supply raw frame deltas
    into the smoothing state pipeline.
    """
    def __init__(self, alpha: float = 0.15) -> None:
        self.alpha: float = alpha
        self.current_ema: float | None = None

    def __rshift__(self, delta: float) -> float:
        """Pipes a raw delta time into the smoother and returns the updated EMA.
        
        Args:
            delta: Raw frame time in milliseconds.
            
        Returns:
            The newly calculated exponential moving average.
        """
        if self.current_ema is None:
            self.current_ema = delta
        else:
            self.current_ema = (self.alpha * delta) + ((1.0 - self.alpha) * self.current_ema)
        return self.current_ema

def process_frame_stream(raw_deltas: Iterable[float]) -> Generator[tuple[float, float], None, None]:
    """Processes a stream of frame deltas into (smoothed_ms, estimated_fps) tuples.
    
    Args:
        raw_deltas: An iterable yielding frame delta durations in milliseconds.
        
    Yields:
        Tuples containing the smoothed frame delta and calculated FPS.
    """
    smoother = FrameDeltaSmoother()
    for delta in raw_deltas:
        smoothed_ms = delta >> smoother
        fps = 1000.0 / smoothed_ms if smoothed_ms > 0 else 0.0
        yield (round(smoothed_ms, 2), round(fps, 1))
