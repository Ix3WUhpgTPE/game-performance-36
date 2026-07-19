import random
import json

class GameError(Exception):
    pass

class Game:
    def __init__(self):
        self.score = 0
        self.level = 1
        self.max_level = 10
        self.is_running = True

    def start_game(self):
        try:
            print('Game started!')
            while self.is_running:
                self.play_level(self.level)
        except GameError as e:
            print(f'Error occurred: {e}')
            self.is_running = False

    def play_level(self, level):
        if level > self.max_level:
            raise GameError('Level exceeds max level!')
        print(f'Playing level {level}')
        outcome = random.choice(['win', 'lose'])
        if outcome == 'win':
            self.score += 10
            print(f'Level {level} completed. Score: {self.score}')
            self.level += 1
        else:
            print(f'Level {level} failed. Better luck next time!')

    def get_score(self):
        return self.score

if __name__ == '__main__':
    game = Game()
    game.start_game()
    score = game.get_score()
    print(f'Final score: {score}')