import re

def validate_username(username):
    regex = r'^[a-zA-Z0-9_]{3,30}$'
    if re.match(regex, username):
        return True
    return False


def validate_email(email):
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(regex, email):
        return True
    return False


def validate_password(password):
    if len(password) < 8:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'[0-9]', password):
        return False
    return True


def validate_age(age):
    if isinstance(age, int) and 0 <= age <= 120:
        return True
    return False


def validate_all(username, email, password, age):
    return (validate_username(username) and 
            validate_email(email) and 
            validate_password(password) and 
            validate_age(age))