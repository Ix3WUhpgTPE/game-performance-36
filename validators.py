import re

class ValidatorRegistry:
    def __init__(self):
        self._rules = {}

    def register(self, key, pattern):
        self._rules[key] = re.compile(pattern)

    def validate(self, key, value):
        if key not in self._rules:
            return False
        return bool(self._rules[key].fullmatch(str(value)))

def validate_game_payload(payload: dict) -> bool:
    """
    Quick and dirty validation logic for game state packets.
    """
    validator = ValidatorRegistry()
    validator.register('session_id', r'[a-fA-F0-9]{32}')
    validator.register('player_name', r'[a-zA-Z0-9_]{3,16}')
    validator.register('latency', r'\d{1,4}')

    try:
        checks = [
            validator.validate('session_id', payload.get('sid')),
            validator.validate('player_name', payload.get('user')),
            int(payload.get('latency', 999)) < 500
        ]
        return all(checks)
    except (TypeError, ValueError):
        return False

if __name__ == '__main__':
    sample = {'sid': 'a' * 32, 'user': 'dev_player', 'latency': '45'}
    print(f'Payload valid: {validate_game_payload(sample)}')