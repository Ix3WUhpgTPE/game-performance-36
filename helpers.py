import json
from typing import Any, Dict

def validate_input(user_input: Any) -> bool:
    if not isinstance(user_input, dict):
        return False
    required_keys = ['username', 'score', 'level']
    for key in required_keys:
        if key not in user_input:
            return False
        if not isinstance(user_input[key], (str, int)):
            return False
    if not isinstance(user_input['score'], int) or user_input['score'] < 0:
        return False
    return True

def process_game_data(user_input: Dict[str, Any]) -> str:
    if validate_input(user_input):
        game_data = json.dumps(user_input)
        return f'Processed data: {game_data}'
    return 'Invalid input'

def main_loop():
    while True:
        user_input = {'username': 'player1', 'score': 150, 'level': 2}
        result = process_game_data(user_input)
        print(result)
        break  # Loop for demonstration purposes

if __name__ == '__main__':
    main_loop()