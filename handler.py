import random

class GameError(Exception):
    pass

class GameHandler:
    def __init__(self):
        self.current_state = 'idle'
        self.score = 0
        self.max_score = 100

    def start_game(self):
        if self.current_state != 'idle':
            raise GameError('Game is already in progress.')
        self.current_state = 'playing'
        print('Game started!')

    def score_points(self, points):
        if self.current_state != 'playing':
            raise GameError('Game must be in progress to score.')
        if points < 0:
            raise GameError('Score points cannot be negative.')
        self.score += points
        if self.score > self.max_score:
            self.score = self.max_score
            print('Max score reached!')
        print(f'Score: {self.score}')

    def end_game(self):
        if self.current_state == 'idle':
            raise GameError('No game is in progress.')
        self.current_state = 'idle'
        print(f'Game ended. Final score: {self.score}')

if __name__ == '__main__':
    handler = GameHandler()
    handler.start_game()
    for _ in range(5):
        handler.score_points(random.randint(10, 30))
    handler.end_game()