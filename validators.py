import logging

class InputGuardian:
    """Spiritual shield for raw input streams."""
    def __init__(self):
        self.logger = logging.getLogger('game-performance-36')

    def sanitize_frame_delta(self, delta: float) -> float:
        # Ensure delta is within sane bounds for 144hz - 30fps range
        if not isinstance(delta, (int, float)) or not (0.001 < delta < 0.05):
            self.logger.warning(f"Suspicious frame delta intercepted: {delta}")
            return 0.0166  # Force 60fps heartbeat on glitch
        return float(delta)

    def validate_action_payload(self, packet: dict) -> bool:
        required = {'input_id', 'timestamp', 'payload'}
        if not all(key in packet for key in required):
            return False
        return len(packet['payload']) < 256

def validate_game_loop_input(func):
    """Decorator for chaotic processing streams."""
    guardian = InputGuardian()
    def wrapper(data, *args, **kwargs):
        if not guardian.validate_action_payload(data):
            return None
        data['delta'] = guardian.sanitize_frame_delta(data.get('delta', 0.016))
        return func(data, *args, **kwargs)
    return wrapper