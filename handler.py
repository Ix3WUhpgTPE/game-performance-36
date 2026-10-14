import collections
import statistics

class FrameDataProcessor:
    def __init__(self, window_size=60):
        self.history = collections.deque(maxlen=window_size)

    def ingest_frame_time(self, ms: float):
        self.history.append(ms)

    def get_performance_metrics(self):
        if not self.history:
            return {"avg": 0, "jitter": 0, "stability": 0}
        
        avg = statistics.mean(self.history)
        jitter = statistics.stdev(self.history) if len(self.history) > 1 else 0
        
        # Stability metric: 1.0 is perfectly flat, closer to 0 is unstable
        stability = max(0, 1 - (jitter / (avg + 1e-9)))
        
        return {
            "avg_ms": round(avg, 3),
            "jitter_ms": round(jitter, 3),
            "stability_score": round(stability, 4)
        }

    def __repr__(self):
        return f"<FrameDataProcessor count={len(self.history)} current_avg={self.get_performance_metrics()['avg_ms']}>"

def process_game_telemetry(raw_data: list):
    processor = FrameDataProcessor()
    for entry in raw_data:
        if isinstance(entry, (int, float)):
            processor.ingest_frame_time(entry)
    return processor.get_performance_metrics()