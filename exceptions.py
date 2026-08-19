class InputValidationError(Exception):
    pass

def validate_input(user_input):
    if not isinstance(user_input, str):
        raise InputValidationError('Input must be a string.')
    if len(user_input) < 1:
        raise InputValidationError('Input cannot be empty.')
    if len(user_input) > 100:
        raise InputValidationError('Input exceeds maximum length of 100 characters.')
    return user_input

if __name__ == '__main__':
    inputs = ['valid_input', '', 123, 'exceeding_length_input_' + 'a' * 92]
    for user_input in inputs:
        try:
            validated_input = validate_input(user_input)
            print(f'Validated Input: {validated_input}')
        except InputValidationError as e:
            print(f'Input error: {e}')