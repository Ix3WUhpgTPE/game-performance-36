import numpy as np

class GameProcessor:
    def __init__(self):
        self.frames = 0
        self.elapsed_time = 0
        self.performance_metrics = {}

    def update_performance_metrics(self, frame_time):
        self.frames += 1
        self.elapsed_time += frame_time
        self.performance_metrics['fps'] = self.frames / self.elapsed_time

    def process_frame(self, frame_data):
        # Perform some computationally intensive operations
        processed_data = self.intensive_computation(frame_data)
        self.update_performance_metrics(self.get_frame_time())
        return processed_data

    def intensive_computation(self, frame_data):
        # Using numpy for optimized computation
        return np.sqrt(frame_data)

    def get_frame_time(self):
        # Return simulated frame time
        return 1.0 / 60  # Simulating 60 FPS

    def reset_metrics(self):
        self.frames = 0
        self.elapsed_time = 0
        self.performance_metrics = {}
        
# Assuming this processor will be instantiated and called within the game loop
