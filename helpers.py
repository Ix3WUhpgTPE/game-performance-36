import random
import math

class GameHelper:
    @staticmethod
    def generate_random_position(game_area_size):
        x = random.randint(0, game_area_size[0])
        y = random.randint(0, game_area_size[1])
        return (x, y)

    @staticmethod
    def calculate_distance(point1, point2):
        return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

    @staticmethod
    def spawn_enemy(enemies, game_area_size):
        if len(enemies) < 10:
            position = GameHelper.generate_random_position(game_area_size)
            enemies.append(position)

    @staticmethod
    def clear_enemies(enemies):
        enemies.clear()

    @staticmethod
    def display_score(score):
        print(f'Score: {score}')