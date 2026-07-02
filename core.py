import time

class GameEngine:
    def __init__(self):
        self.entities = []
        self.last_update_time = time.time()

    def add_entity(self, entity):
        self.entities.append(entity)

    def update(self):
        current_time = time.time()
        delta_time = current_time - self.last_update_time
        self.last_update_time = current_time
        self.optimize_entities(delta_time)

    def optimize_entities(self, delta_time):
        for entity in self.entities:
            entity.update(delta_time)
            if entity.should_remove():
                self.entities.remove(entity)

class Entity:
    def __init__(self, name):
        self.name = name
        self.active = True

    def update(self, delta_time):
        # Update entity logic here
        pass

    def should_remove(self):
        return not self.active

# Example usage:
if __name__ == '__main__':
    engine = GameEngine()
    engine.add_entity(Entity('Player1'))
    while True:
        engine.update()