import time
import numpy as np
from functools import lru_cache

class GameProcessor:
    def __init__(self, data):
        self.data = np.array(data)

    @lru_cache(maxsize=128)
    def calculate_performance_metrics(self, player_stats):
        # Simulating expensive computation
        time.sleep(0.1)
        return np.mean(player_stats), np.std(player_stats)

    def process_data(self):
        metrics = []
        for stats in self.data:
            mean, std = self.calculate_performance_metrics(tuple(stats))
            metrics.append((mean, std))
        return metrics

if __name__ == '__main__':
    sample_data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    processor = GameProcessor(sample_data)
    results = processor.process_data()
    print(results)