import re

class GameDataValidator:
    @staticmethod
    def validate_score(score):
        if not isinstance(score, int) or score < 0:
            raise ValueError('Score must be a non-negative integer.')
        return True

    @staticmethod
    def validate_username(username):
        if not isinstance(username, str) or not re.match('^[A-Za-z0-9_]{3,20}$', username):
            raise ValueError('Username must be 3-20 characters long and can contain letters, numbers, and underscores.')
        return True

    @staticmethod
    def validate_game_id(game_id):
        if not isinstance(game_id, str) or not game_id.isdigit() or len(game_id) != 10:
            raise ValueError('Game ID must be a string of 10 digits.')
        return True

if __name__ == '__main__':
    # Example usage
    try:
        GameDataValidator.validate_score(100)
        GameDataValidator.validate_username('Player_1')
        GameDataValidator.validate_game_id('1234567890')
        print('All validations passed.')
    except ValueError as e:
        print(e)