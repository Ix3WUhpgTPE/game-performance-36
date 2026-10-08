import logging
from typing import Any, Dict, Optional

def validate_frame_input(data: Dict[str, Any]) -> bool:
    """
    Sanitizes raw input stream for frame processing pipelines.
    Uses a strictly typed threshold to filter noise and malformed telemetry.
    """
    required_keys = {'ts', 'fps', 'lat'}
    if not all(k in data for k in required_keys):
        return False

    try:
        fps = float(data['fps'])
        lat = float(data['lat'])
        # Performance sanity check: frame time cannot be negative
        # discard impossible spikes above 2000fps or below 0
        if not (0 <= fps <= 2000) or lat < 0:
            return False
    except (ValueError, TypeError):
        return False

    return True

def process_validated_stream(stream: list) -> list:
    """
    Generator wrapper to consume valid input chunks.
    """
    return [frame for frame in stream if validate_frame_input(frame)]

def log_validation_error(ctx: str) -> None:
    logging.warning(f"dropped malicious or malformed input sequence: {ctx}")