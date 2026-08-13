def validate_input(user_input):
    if not isinstance(user_input, str):
        return False
    if any(char in user_input for char in ['$', '%', '^']):
        return False
    return True

def main_processing_loop():
    while True:
        user_input = input('Enter command: ')
        if not validate_input(user_input):
            print('Invalid input, please try again.');
            continue
        # Continue processing the validated input
        print(f'Processing: {user_input}')

if __name__ == '__main__':
    main_processing_loop()