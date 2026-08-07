import re

def validate_input(user_input):
    if not isinstance(user_input, str):
        raise ValueError('Input must be a string')
    if len(user_input) == 0:
        raise ValueError('Input cannot be empty')
    if not re.match('^[a-zA-Z0-9_]*$', user_input):
        raise ValueError('Input can only contain alphanumeric characters and underscores')
    return True

def process_game_input(user_input):
    try:
        validate_input(user_input)
        # Game input processing logic goes here
        return f'Processed input: {user_input}'
    except ValueError as e:
        return str(e)

if __name__ == '__main__':
    test_inputs = ['valid_input123', '', 'invalid@input', 42]
    for input_val in test_inputs:
        print(process_game_input(input_val))