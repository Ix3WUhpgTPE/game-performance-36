import time
import functools
import logging

logger = logging.getLogger('game-performance-36')

def resilient_network_call(max_retries=3, delay=1.5, backoff=2):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            current_delay = delay
            while attempts < max_retries:
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    attempts += 1
                    if attempts >= max_retries:
                        logger.error(f'failed after {max_retries} attempts')
                        raise
                    time.sleep(current_delay)
                    current_delay *= backoff
            return None
        return wrapper
    return decorator

class NetworkProcessor:
    @resilient_network_call(max_retries=4)
    def sync_game_state(self, packet):
        # simulated jittery network socket send
        import random
        if random.random() < 0.7:
            raise ConnectionError('Packet dropped by carrier')
        return {'status': 'delivered'}