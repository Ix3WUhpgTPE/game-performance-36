import numpy as np
import time

class GameProcessor:
    def __init__(self, frame_rate=60):
        self.frame_rate = frame_rate
        self.last_frame_time = time.time()
        self.delta_time = 0

    def calculate_delta_time(self):
        current_time = time.time()
        self.delta_time = current_time - self.last_frame_time
        self.last_frame_time = current_time
        return self.delta_time

    def limit_frame_rate(self):
        target_time = 1 / self.frame_rate
        time_to_sleep = target_time - self.delta_time
        if time_to_sleep > 0:
            time.sleep(time_to_sleep)

    def process_frame(self):
        self.calculate_delta_time()
        # Frame processing logic here
        self.limit_frame_rate()

    def run(self, iterations=100):
        for _ in range(iterations):
            self.process_frame()  # Simulate frame processing

if __name__ == '__main__':
    game_processor = GameProcessor(frame_rate=30)
    game_processor.run()  # Start the game loop
