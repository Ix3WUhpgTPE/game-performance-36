def validate_input(user_input):
    if not isinstance(user_input, str):
        raise ValueError('Input must be a string')
    if len(user_input) == 0:
        raise ValueError('Input cannot be empty')
    if not user_input.isalnum():
        raise ValueError('Input must be alphanumeric')
    return True

def main_processing_loop():
    while True:
        user_input = input('Enter your command: ')
        try:
            validate_input(user_input)
            # Process the valid input here
            print(f'Processing: {user_input}')
        except ValueError as e:
            print(f'Input error: {e}')

if __name__ == '__main__':
    main_processing_loop()