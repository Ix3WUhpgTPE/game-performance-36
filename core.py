import time
import random

class Game:
    def __init__(self):
        self.players = []
        self.score = 0
    
    def add_player(self, name):
        self.players.append(name)
        print(f'{name} joined the game!')
    
    def play_round(self):
        round_score = random.randint(1, 10)
        self.score += round_score
        print(f'Round score: {round_score}, Total score: {self.score}')
    
    def get_performance(self):
        return self.score / len(self.players) if self.players else 0
    
    def optimize_performance(self):
        start = time.time()
        for _ in range(1000):
            self.play_round()
        end = time.time()
        print(f'Optimized performance over 1000 rounds took {end - start:.2f} seconds')

if __name__ == '__main__':
    game = Game()
    game.add_player('Alice')
    game.add_player('Bob')
    game.optimize_performance()
    print(f'Game performance: {game.get_performance():.2f}')