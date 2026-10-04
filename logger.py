import sys
import functools
import traceback

def performance_trap(fallback_val=None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except (MemoryError, RuntimeError) as e:
                sys.stderr.write(f'[CRITICAL-PERF] {func.__name__} failed: {str(e)}\n')
                return fallback_val
            except Exception as e:
                sys.stderr.write(f'[ENGINE-STUTTER] {func.__name__} recovered: {type(e).__name__}\n')
                traceback.print_exc(file=sys.stderr)
                return fallback_val
        return wrapper
    return decorator

class GameLogger:
    def __init__(self):
        self.log_file = 'game_stats.log'

    @performance_trap(fallback_val=False)
    def write_frame_metric(self, metric: str, value: float) -> bool:
        with open(self.log_file, 'a') as f:
            f.write(f'{metric}: {value:.4f}\n')
        return True

    @staticmethod
    def emergency_dump(data: dict):
        try:
            import json
            with open('crash_dump.json', 'w') as f:
                json.dump(data, f)
        except (TypeError, OSError):
            pass