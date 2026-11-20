import math
from typing import List, Dict, Union

class TelemetryCruncher:
    def __init__(self, sensitivity: float = 1.0):
        self.sensitivity = sensitivity

    def smooth_input_data(self, samples: List[float]) -> List[float]:
        if not samples:
            return []
        return [math.tanh(x * self.sensitivity) for x in samples]

    def calculate_dps_burst(self, hits: List[Dict[str, float]], window_size: int = 5) -> float:
        if len(hits) < window_size:
            return sum(h['damage'] for h in hits)
        
        slices = [sum(h['damage'] for h in hits[i:i+window_size]) 
                  for i in range(len(hits) - window_size + 1)]
        return max(slices) if slices else 0.0

    @staticmethod
    def normalize_vectors(data: List[List[float]]) -> List[List[float]]:
        return [[v / math.sqrt(sum(x**2 for x in vec)) for v in vec] for vec in data]

def process_game_state(payload: Union[List[float], Dict]) -> Dict:
    if isinstance(payload, list):
        return {'status': 'processed', 'data': TelemetryCruncher().smooth_input_data(payload)}
    return {'status': 'error', 'reason': 'invalid payload structure'}