def validate_input(user_input):
    if not isinstance(user_input, dict):
        raise ValueError('Input must be a dictionary')
    if 'action' not in user_input:
        raise ValueError('Missing action key')
    if user_input['action'] not in ['move', 'attack', 'defend']:
        raise ValueError('Invalid action specified')
    return True

def main_loop():
    while True:
        user_input = get_user_input()
        try:
            validate_input(user_input)
            process_action(user_input['action'])
        except ValueError as e:
            print(f'Input error: {e}')
            continue
        except Exception as e:
            print(f'Unexpected error: {e}')

        # Other game logic goes here

def get_user_input():
    # Simulating user input for the demo
    return {'action': 'move'}  # Replace with actual input source


def process_action(action):
    print(f'Processing action: {action}')

if __name__ == '__main__':
    main_loop()