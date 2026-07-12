import json
from collections import defaultdict

def load_game_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def aggregate_score_data(game_data):
    score_summary = defaultdict(lambda: {'total_score': 0, 'games_played': 0})
    for entry in game_data:
        player = entry['player']
        score_summary[player]['total_score'] += entry['score']
        score_summary[player]['games_played'] += 1
    return score_summary


def get_high_scores(score_data, top_n=5):
    sorted_scores = sorted(score_data.items(), key=lambda x: x[1]['total_score'], reverse=True)
    return sorted_scores[:top_n]


def save_high_scores(high_scores, output_path):
    with open(output_path, 'w') as file:
        json.dump(high_scores, file, indent=4)


def process_game_scores(input_file, output_file, top_n=5):
    game_data = load_game_data(input_file)
    aggregated_scores = aggregate_score_data(game_data)
    high_scores = get_high_scores(aggregated_scores, top_n)
    save_high_scores(high_scores, output_file)