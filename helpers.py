def safe_divide(numerator, denominator):
    try:
        if denominator == 0:
            raise ValueError('Denominator cannot be zero.')
        return numerator / denominator
    except TypeError:
        raise TypeError('Numerator and denominator must be numbers.')


def get_player_score(player):
    try:
        if player is None:
            raise ValueError('Player cannot be None.')
        return player['score']
    except KeyError:
        raise KeyError('Score key is missing.')
    except TypeError:
        raise TypeError('Player must be a dictionary.')


def load_game_data(file_path):
    import json
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f'File not found: {file_path}')
    except json.JSONDecodeError:
        raise ValueError('File is not a valid JSON.')