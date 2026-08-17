import re

def is_valid_username(username):
    pattern = '^[a-zA-Z0-9_]{3,16}$'
    return bool(re.match(pattern, username))


def is_valid_email(email):
    pattern = '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


def is_valid_password(password):
    if len(password) < 8:
        return False
    has_digit = any(char.isdigit() for char in password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    return has_digit and has_upper and has_lower


def validate_user_data(username, email, password):
    if not is_valid_username(username):
        return 'Invalid username'
    if not is_valid_email(email):
        return 'Invalid email'
    if not is_valid_password(password):
        return 'Invalid password'
    return 'User data is valid'