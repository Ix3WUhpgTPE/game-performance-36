import json
import os

def load_game_data(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Data file not found: {file_path}")
    with open(file_path, 'r') as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            raise ValueError(f"Error decoding JSON from {file_path}")
    return data

def save_game_data(file_path, data):
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    except IOError:
        raise IOError(f"Unable to write to {file_path}")

def get_data_statistics(data):
    stats = {
        'total_players': len(data['players']),
        'highest_score': max(player['score'] for player in data['players']),
        'average_score': sum(player['score'] for player in data['players']) / len(data['players'])
    }
    return stats

# Example usage
if __name__ == '__main__':
    example_data = {'players': [{'name': 'Player1', 'score': 100}, {'name': 'Player2', 'score': 200}]}
    save_game_data('game_data.json', example_data)
    loaded_data = load_game_data('game_data.json')
    print(get_data_statistics(loaded_data))