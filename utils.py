import time
import numpy as np

class PerformanceUtils:
    @staticmethod
    def time_this(func):
        """Decorator to measure the performance of a function."""
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            print(f"{func.__name__} executed in {end_time - start_time:.4f} seconds")
            return result
        return wrapper
    
    @staticmethod
    def optimize_array_operations(arr):
        """Optimizes operations on numpy arrays using vectorization."""
        arr = np.array(arr)
        optimized_result = np.where(arr > 0, arr * 2, arr * -1)
        return optimized_result

# Example usage:
if __name__ == '__main__':
    utils = PerformanceUtils()
    result = utils.optimize_array_operations([1, -1, 2, -2])
    print(result)