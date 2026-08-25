import json
from collections import Counter

def process_gaming_data(raw_data):
    try:
        data = json.loads(raw_data)
    except (json.JSONDecodeError, TypeError):
        data = []
    if not isinstance(data, list):
        data = [data] if data else []

    player_stats = Counter()
    performance_scores = []

    for entry in data:
        if isinstance(entry, dict):
            player = entry.get('player', 'unknown')
            score = entry.get('score', 0)
            kills = entry.get('kills', 0)
            synergy = (score * 0.6 + kills * 0.4) ** 0.5
            player_stats[player] += synergy
            performance_scores.append(synergy)

    if not performance_scores:
        return {"total_performance": 0, "top_player": None, "average_synergy": 0}

    total_perf = sum(performance_scores)
    avg_synergy = total_perf / len(performance_scores)

    top_player = player_stats.most_common(1)[0][0] if player_stats else None

    sorted_scores = sorted(performance_scores)
    n = len(sorted_scores)
    if n % 2 == 1:
        median = sorted_scores[n//2]
    else:
        median = (sorted_scores[n//2-1] + sorted_scores[n//2]) / 2

    return {
        "total_performance": round(total_perf, 2),
        "top_player": top_player,
        "average_synergy": round(avg_synergy, 2),
        "median_synergy": round(median, 2),
        "player_distribution": dict(player_stats)
    }

if __name__ == "__main__":
    sample_data = '[{"player": "Alex", "score": 1500, "kills": 25}, {"player": "Sam", "score": 1200, "kills": 18}, {"player": "Alex", "score": 1800, "kills": 30}]'
    result = process_gaming_data(sample_data)
    print(result)
