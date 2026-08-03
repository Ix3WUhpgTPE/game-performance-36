import time
import numpy as np

class GameEngine:
    def __init__(self):
        self.entities = []
        self.delta_time = 0

    def add_entity(self, entity):
        self.entities.append(entity)

    def update_entities(self):
        start_time = time.perf_counter()
        for entity in self.entities:
            entity.update(self.delta_time)
        self.delta_time = time.perf_counter() - start_time

    def calculate_average_frame_time(self, frame_times):
        filtered_frame_times = list(filter(lambda x: x < 1 / 30, frame_times))
        return np.mean(filtered_frame_times) if filtered_frame_times else 0

class Entity:
    def __init__(self, name):
        self.name = name
        self.position = np.array([0, 0])

    def update(self, delta_time):
        # Simulate some position update logic
        self.position += np.array([delta_time * 10, delta_time * 5])

# Example usage
if __name__ == '__main__':
    engine = GameEngine()
    engine.add_entity(Entity('Player'))
    for _ in range(5):
        engine.update_entities()
    