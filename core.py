import random
import time

class Game:
    def __init__(self, name, players):
        self.name = name
        self.players = players
        self.scores = {player: 0 for player in players}

    def start_game(self):
        print(f'Starting game: {self.name}')
        self.play_rounds(5)

    def play_rounds(self, rounds):
        for round_number in range(1, rounds + 1):
            self.play_round(round_number)

    def play_round(self, round_number):
        print(f'Round {round_number}')
        for player in self.players:
            score = self.roll_dice()
            self.scores[player] += score
            print(f'{player} rolled a {score}')
        self.display_scores()

    def roll_dice(self):
        return random.randint(1, 6)

    def display_scores(self):
        print('Current Scores:')
        for player, score in self.scores.items():
            print(f'{player}: {score}')

if __name__ == '__main__':
    players = ['Alice', 'Bob', 'Charlie']
    game = Game('Dice Game', players)
    game.start_game()