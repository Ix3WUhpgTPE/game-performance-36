import re

def is_valid_username(username):
    pattern = r'^[a-zA-Z0-9_]{3,16}$'
    return bool(re.match(pattern, username))


def is_valid_password(password):
    min_length = 8
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    return (len(password) >= min_length and has_upper and has_lower and has_digit)


def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


def validate_user_data(username, password, email):
    return (is_valid_username(username) and 
            is_valid_password(password) and 
            is_valid_email(email))


if __name__ == '__main__':
    print(validate_user_data('user_name', 'Password123', 'user@example.com'))  # Test the validation
