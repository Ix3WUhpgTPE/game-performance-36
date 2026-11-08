import re
from typing import Any, Dict, List

class GameSchemaValidator:
    def __init__(self, required_keys: List[str]):
        self.required_keys = required_keys
        self.pattern = re.compile(r'^[a-zA-Z0-9_]{3,20}$')

    def validate_entity(self, data: Dict[str, Any]) -> bool:
        if not all(key in data for key in self.required_keys):
            return False
        return all(isinstance(v, str) and self.pattern.match(v) for v in data.values())

def sanitize_input(user_input: str) -> str:
    return ''.join(char for char in user_input if char.isalnum())

def check_frame_budget(fps: float, threshold: float = 60.0) -> bool:
    return fps >= threshold

class PerformanceConstraint:
    def __init__(self, tolerance: float):
        self.tolerance = tolerance

    def check(self, val: float) -> bool:
        return abs(val) < self.tolerance

if __name__ == '__main__':
    validator = GameSchemaValidator(['id', 'tag'])
    print(validator.validate_entity({'id': 'p1', 'tag': 'warrior'}))