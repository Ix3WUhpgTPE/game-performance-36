import numpy as np

class GamePerformanceOptimizer:
    def __init__(self):
        self.cache = {}

    def optimized_function(self, input_data):
        if input_data in self.cache:
            return self.cache[input_data]
        result = self.perform_heavy_computation(input_data)
        self.cache[input_data] = result
        return result

    def perform_heavy_computation(self, input_data):
        # Simulating a heavy computation using numpy
        array = np.array(input_data)
        return np.sum(array ** 2)  # Example operation

    def clear_cache(self):
        self.cache.clear()

optimizer = GamePerformanceOptimizer()

# Example usage:
# result = optimizer.optimized_function([1, 2, 3])
# print(result)
