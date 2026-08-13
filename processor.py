import json
from typing import List, Dict, Any

class GameDataProcessor:
    def __init__(self, data: List[Dict[str, Any]]) -> None:
        self.data = data

    def filter_by_score(self, threshold: float) -> List[Dict[str, Any]]:
        return [entry for entry in self.data if entry.get('score', 0) >= threshold]

    def aggregate_scores(self) -> Dict[str, float]:
        score_aggregation = {}
        for entry in self.data:
            player = entry.get('player', 'Unknown')
            score_aggregation[player] = score_aggregation.get(player, 0) + entry.get('score', 0)
        return score_aggregation

    def to_json(self) -> str:
        return json.dumps(self.data, indent=4)

# Sample usage
if __name__ == '__main__':
    sample_data = [
        {'player': 'Alice', 'score': 150},
        {'player': 'Bob', 'score': 300},
        {'player': 'Alice', 'score': 200},
    ]
    processor = GameDataProcessor(sample_data)
    print(processor.filter_by_score(200))
    print(processor.aggregate_scores())
    print(processor.to_json())
