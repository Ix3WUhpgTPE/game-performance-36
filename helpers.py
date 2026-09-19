import functools
import logging
from typing import Callable, Any

logger = logging.getLogger('game-performance-36')

class PerformanceLimitExceeded(Exception):
    """Raised when metrics fall outside of acceptable frame budgets."""
    pass

def robust_execute(func: Callable):
    """Wraps game engine tasks with defensive boundary checks."""
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        try:
            result = func(*args, **kwargs)
            if result is None:
                raise ValueError('Null return in critical path')
            return result
        except (ZeroDivisionError, TypeError, KeyError) as e:
            logger.error(f'Metric calculation error in {func.__name__}: {e}')
            return 0.0
        except Exception as e:
            logger.critical(f'Unexpected engine crash: {e}')
            raise PerformanceLimitExceeded(f'Task {func.__name__} failed critical state')
    return wrapper

@robust_execute
def calculate_frame_time(delta: float, target: float) -> float:
    return target / delta

def validate_resource_load(resource_map: dict, key: str) -> bool:
    """Verifies asset existence without raising fatal lookup errors."""
    try:
        return resource_map[key] is not None
    except (KeyError, TypeError):
        logger.warning(f'Resource {key} missing, falling back to default')
        return False