import re

def is_valid_email(email):
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(regex, email) is not None


def is_valid_username(username):
    return len(username) >= 3 and len(username) <= 20 and username.isalnum()


def is_valid_password(password):
    return (len(password) >= 8 and
            any(char.isdigit() for char in password) and
            any(char.islower() for char in password) and
            any(char.isupper() for char in password) and
            any(char in '!@#$%^&*()-+=' for char in password))


def is_within_bounds(value, min_value, max_value):
    return min_value <= value <= max_value


def is_positive_integer(value):
    return isinstance(value, int) and value > 0
