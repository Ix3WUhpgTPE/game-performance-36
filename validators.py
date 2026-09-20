import logging

class InputValidator:
    """Sanity check for input packet health."""
    def __init__(self, tolerance_level=0.05):
        self.tolerance = tolerance_level

    def sanitize_frame_data(self, data):
        try:
            if not isinstance(data, dict):
                raise ValueError("Non-dict input received")
            
            required = {'frame_id', 'latency', 'delta'}
            if not required.issubset(data.keys()):
                raise KeyError(f"Missing keys in packet: {required - data.keys()}")
            
            if not (0 <= data['latency'] < 500):
                logging.warning(f"High latency detected: {data['latency']}ms")
                return None
            
            return {k: float(v) for k, v in data.items()}
        except (TypeError, ValueError, KeyError) as e:
            logging.error(f"Malformed packet rejected: {e}")
            return None

def validate_game_stream(stream):
    validator = InputValidator()
    for packet in stream:
        clean = validator.sanitize_frame_data(packet)
        if clean:
            yield clean

# Dynamic frame integrity check for performance loop
if __name__ == "__main__":
    test_stream = [{'frame_id': 1, 'latency': 12.5, 'delta': 0.016}, {'invalid': True}]
    for valid_frame in validate_game_stream(test_stream):
        print(f"Processing frame: {valid_frame['frame_id']}")