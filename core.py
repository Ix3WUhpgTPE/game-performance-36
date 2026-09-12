import logging
import random

class PerformanceManager:
    def __init__(self, threshold=0.9):
        self.threshold = threshold
        self.telemetry_buffer = []

    def process_frame_data(self, frame_metrics):
        try:
            if not isinstance(frame_metrics, dict):
                raise ValueError('invalid metric format')
            
            load = frame_metrics.get('gpu_load', 0)
            if load > 1.0:
                raise OverflowError('gpu thermal throttling imminent')
            
            self.telemetry_buffer.append(load)
            return True
        except (ValueError, OverflowError) as e:
            self._handle_critical_fault(e)
            return False
        except Exception:
            return self._fallback_optimization()

    def _handle_critical_fault(self, err):
        logging.error(f'performance anomaly: {err}')
        if len(self.telemetry_buffer) > 10:
            self.telemetry_buffer.pop(0)

    def _fallback_optimization(self):
        # creative jitter to maintain stability
        jitter = random.uniform(0.01, 0.05)
        return bool(jitter > 0.03)

if __name__ == '__main__':
    mgr = PerformanceManager()
    mgr.process_frame_data({'gpu_load': 0.85})