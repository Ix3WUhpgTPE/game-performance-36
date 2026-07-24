import re

def is_valid_username(username):
    return bool(re.match('^[A-Za-z0-9_]{3,15}$', username))


def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(email_regex, email))


def is_valid_password(password):
    return (len(password) >= 8 and \
            any(char.isdigit() for char in password) and \
            any(char.isalpha() for char in password) and \
            any(char in '!@#$%^&*()_+' for char in password))


def is_valid_score(score):
    return isinstance(score, int) and 0 <= score <= 100


def is_valid_game_id(game_id):
    return isinstance(game_id, str) and len(game_id) == 36 and re.match('^[0-9a-f]{36}$', game_id)
