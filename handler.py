from collections import deque
from typing import Deque, Generator, Optional, Tuple

class FrameSpikeHandler:
    """A highly reactive handler to detect frame-rate micro-stutters during gameplay.

    Utilizes a co-routine generator structure to ingest frame times dynamically
    and output performance anomalies when render spikes surpass dynamic thresholds.
    """

    def __init__(self, window_size: int = 60, spike_threshold_factor: float = 2.5) -> None:
        self.window_size: int = window_size
        self.threshold_factor: float = spike_threshold_factor
        self.history: Deque[float] = deque(maxlen=window_size)

    def pipeline(self) -> Generator[Optional[Tuple[float, float]], float, None]:
        """A coroutine-based pipeline consuming raw frame times (ms).

        Yields a tuple of (actual_frame_time, threshold) if a spike (anomaly) is detected,
        otherwise yields None.
        """
        frame_time: Optional[float] = yield None

        while True:
            if frame_time is None:
                frame_time = yield None
                continue

            anomaly: Optional[Tuple[float, float]] = None
            if len(self.history) >= 10:
                average: float = sum(self.history) / len(self.history)
                dynamic_limit: float = average * self.threshold_factor
                if frame_time > dynamic_limit:
                    anomaly = (frame_time, dynamic_limit)

            self.history.append(frame_time)
            frame_time = yield anomaly