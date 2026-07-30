import re

class Validator:
    def __init__(self, username_min_length=3, username_max_length=20):
        self.username_min_length = username_min_length
        self.username_max_length = username_max_length

    def is_valid_username(self, username):
        if not isinstance(username, str):
            return False
        if not (self.username_min_length <= len(username) <= self.username_max_length):
            return False
        if not re.match('^[a-zA-Z0-9_]+$', username):
            return False
        return True

    def is_valid_email(self, email):
        if not isinstance(email, str):
            return False
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(email_regex, email))

    def is_valid_password(self, password):
        if not isinstance(password, str):
            return False
        return 8 <= len(password) <= 128

    def validate_user(self, username, email, password):
        return (self.is_valid_username(username) and 
                self.is_valid_email(email) and 
                self.is_valid_password(password))