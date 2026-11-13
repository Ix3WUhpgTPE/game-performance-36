import logging
from typing import Any, Dict, Optional

logger = logging.getLogger('game-performance-36')

class InputValidator:
    """Sanity check for raw game metrics payload."""
    def __init__(self, schema: Dict[str, type]):
        self.schema = schema

    def validate(self, payload: Any) -> Optional[Dict[str, Any]]:
        try:
            if not isinstance(payload, dict):
                raise ValueError(f"Payload must be dict, got {type(payload).__name__}")
            
            cleaned = {}
            for key, expected_type in self.schema.items():
                value = payload.get(key)
                if value is None or not isinstance(value, expected_type):
                    raise TypeError(f"Field {key} missing or invalid type: {type(value)}")
                cleaned[key] = value
            return cleaned
        except (ValueError, TypeError) as e:
            logger.error(f"Invalid input frame dropped: {e}")
            return None

def sanitize_tick_data(data: Any) -> Optional[Dict[str, Any]]:
    """Quick validation for core frame metrics."""
    validator = InputValidator({
        "fps": int,
        "frame_time": float,
        "player_id": int
    })
    return validator.validate(data)