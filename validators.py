def validate_input(user_input):
    if not isinstance(user_input, str):
        raise ValueError('Input must be a string.')
    if not user_input:
        raise ValueError('Input cannot be empty.')
    if len(user_input) > 100:
        raise ValueError('Input too long, max 100 characters.')
    return True

if __name__ == '__main__':
    try:
        user_input = input('Enter your command: ')
        validate_input(user_input)
        print('Valid input!')
    except ValueError as e:
        print(f'Error: {e}')