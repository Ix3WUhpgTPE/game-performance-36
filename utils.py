import json
import os

class GameDataHandler:
    def __init__(self, filepath):
        self.filepath = filepath
        self.data = self.load_data()

    def load_data(self):
        if os.path.exists(self.filepath):
            with open(self.filepath, 'r') as file:
                return json.load(file)
        return {}

    def save_data(self):
        with open(self.filepath, 'w') as file:
            json.dump(self.data, file, indent=4)

    def update_score(self, player, score):
        if player in self.data:
            self.data[player]['score'] += score
        else:
            self.data[player] = {'score': score}
        self.save_data()

    def get_top_players(self, n=5):
        sorted_players = sorted(self.data.items(), key=lambda item: item[1]['score'], reverse=True)
        return sorted_players[:n]

if __name__ == '__main__':
    handler = GameDataHandler('game_scores.json')
    handler.update_score('Alice', 10)
    handler.update_score('Bob', 20)
    print(handler.get_top_players(2))