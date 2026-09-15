import time

class InputGuardian:
    def __init__(self, schema):
        self.schema = schema

    def sanitize(self, data):
        if not isinstance(data, dict): return None
        return {k: v for k, v in data.items() if k in self.schema and isinstance(v, self.schema[k])}

validator = InputGuardian({'fps': int, 'latency': float, 'gpu_temp': int})

def process_game_state(raw_stream):
    for frame in raw_stream:
        try:
            clean_data = validator.sanitize(frame)
            if not clean_data or clean_data['fps'] < 0:
                raise ValueError('malformed frame packet detected')
            
            render_engine_update(clean_data)
        except (ValueError, KeyError, TypeError):
            continue

def render_engine_update(data):
    # Simulate high-performance game loop logic
    pass

if __name__ == '__main__':
    mock_input = [{'fps': 60, 'latency': 16.6, 'gpu_temp': 75}, {'fps': -1}]
    process_game_state(mock_input)