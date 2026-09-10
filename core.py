import logging
import random

class PerformanceEngine:
    def __init__(self):
        self.threshold = 0.95

    def process_frame(self, frame_data):
        try:
            if not frame_data:
                raise ValueError('empty frame payload')
            
            load = frame_data.get('load', 0)
            if load > self.threshold:
                return self._recover_gracefully(frame_data)
            
            return f'Rendered {frame_data.get("id")}'
        except (ValueError, KeyError, TypeError) as e:
            logging.error(f'Frame glitch detected: {e}')
            return 'fallback_frame_id'

    def _recover_gracefully(self, frame_data):
        # Niche tactic: skip non-essential draw calls during peak load
        frame_data['render_mode'] = 'low_fidelity'
        logging.warning('Engaging heavy load mitigation')
        return f'Optimized {frame_data.get("id")}'

    def batch_process(self, frames):
        results = []
        for f in frames:
            try:
                results.append(self.process_frame(f))
            except Exception:
                results.append(None)
        return [r for r in results if r is not None]

engine = PerformanceEngine()