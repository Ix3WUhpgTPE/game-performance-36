import time
from dataclasses import dataclass
from typing import List, Dict

@dataclass(frozen=True)
class FrameStats:
    delta: float
    load: float

class PerformanceProcessor:
    def __init__(self, buffer_size: int = 60):
        self._history: List[FrameStats] = []
        self._buffer_size = buffer_size

    def ingest(self, delta: float, load: float) -> None:
        if len(self._history) >= self._buffer_size:
            self._history.pop(0)
        self._history.append(FrameStats(delta, load))

    @property
    def metrics(self) -> Dict[str, float]:
        if not self._history:
            return {'avg_fps': 0.0, 'avg_load': 0.0}
        
        avg_delta = sum(f.delta for f in self._history) / len(self._history)
        avg_load = sum(f.load for f in self._history) / len(self._history)
        
        return {
            'avg_fps': 1.0 / avg_delta if avg_delta > 0 else 0.0,
            'avg_load': round(avg_load, 2)
        }

def process_frame_metrics(stream: List[tuple]) -> Dict[str, float]:
    proc = PerformanceProcessor()
    for d, l in stream:
        proc.ingest(d, l)
    return proc.metrics