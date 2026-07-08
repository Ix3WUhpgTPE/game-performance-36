import re

class GameDataValidator:
    @staticmethod
    def is_valid_game_id(game_id):
        return isinstance(game_id, str) and re.match(r'^[A-Z0-9]{10}$', game_id)

    @staticmethod
    def is_valid_score(score):
        return isinstance(score, (int, float)) and 0 <= score <= 100

    @staticmethod
    def is_valid_username(username):
        return isinstance(username, str) and 3 <= len(username) <= 20 and re.match(r'^[A-Za-z0-9_]+$', username)

    @staticmethod
    def validate_game_data(game_id, score, username):
        if not GameDataValidator.is_valid_game_id(game_id):
            raise ValueError('Invalid game ID format.')
        if not GameDataValidator.is_valid_score(score):
            raise ValueError('Score must be between 0 and 100.')
        if not GameDataValidator.is_valid_username(username):
            raise ValueError('Username must be 3-20 characters long and contain only letters, numbers, and underscores.')
        return True
