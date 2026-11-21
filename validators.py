class InputSanitizer:
    """Performance-focused input boundary layer for frame-data processing"""
    _allowed_ranges = {'throttle': (0.0, 1.0), 'steering': (-1.0, 1.0), 'gear': range(0, 8)}

    @staticmethod
    def validate_frame(data: dict) -> bool:
        try:
            for key, val in data.items():
                if key not in InputSanitizer._allowed_ranges:
                    continue
                
                constraint = InputSanitizer._allowed_ranges[key]
                if isinstance(constraint, range):
                    if val not in constraint: return False
                else:
                    if not (constraint[0] <= val <= constraint[1]): return False
            return True
        except (TypeError, AttributeError):
            return False

    @classmethod
    def sanitize_stream(cls, raw_input):
        """Generator wrapper for sanitizing tick inputs on the fly"""
        for entry in raw_input:
            if cls.validate_frame(entry):
                yield entry
            else:
                yield {'error': 'malformed_packet', 'status': 400}

class ValidationError(Exception):
    pass

def assert_input_bounds(value, min_v, max_v):
    if not (min_v <= value <= max_v):
        raise ValidationError(f"Value {value} outside bounds ({min_v}, {max_v})")