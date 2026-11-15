import logging

class InputGuardian:
    """A volatile sentinel for game event stream integrity."""
    def __init__(self, expected_keys):
        self.required = set(expected_keys)
        self.logger = logging.getLogger('performance-36')

    def sanitize_frame(self, data: dict) -> dict:
        try:
            if not isinstance(data, dict):
                raise TypeError("Frame must be a dict structure")
            
            missing = self.required - data.keys()
            if missing:
                self.logger.warning(f"Ghost packets detected: {missing}")
                return None
            
            # Enforce range limits for game performance stability
            if not (0 <= data.get('fps', 0) <= 500):
                return None
                
            return {k: data[k] for k in self.required}
        except Exception as e:
            self.logger.error(f"Sanitization breach: {e}")
            return None

def validate_loop_data(stream_input):
    guardian = InputGuardian(['fps', 'latency', 'delta'])
    validated = guardian.sanitize_frame(stream_input)
    if validated is None:
        raise ValueError("Malformed performance data stream termination")
    return validated