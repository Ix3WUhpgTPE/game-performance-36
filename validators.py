import re

def validate_username(username):
    if not (3 <= len(username) <= 20):
        return False
    if not re.match('^[a-zA-Z0-9_]*$', username):
        return False
    return True


def validate_password(password):
    if not (8 <= len(password) <= 50):
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char in '!@#$%^&*()_+-=[]{}|;:,.<>?/' for char in password):
        return False
    return True


def validate_email(email):
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(regex, email))
