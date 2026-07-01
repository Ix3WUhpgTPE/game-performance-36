import random
import json

def validate_input(user_input):
    if not isinstance(user_input, dict):
        raise ValueError('Input must be a dictionary.')
    if 'action' not in user_input:
        raise ValueError('Missing action key in input.')
    if user_input['action'] not in ['start', 'stop', 'pause']:
        raise ValueError('Invalid action value.')
    return True

def game_loop():
    print('Game is starting...')
    while True:
        try:
            user_input = json.loads(input('Enter a command (JSON format): '))
            validate_input(user_input)
            if user_input['action'] == 'start':
                print('Game started!')
            elif user_input['action'] == 'stop':
                print('Game stopped!')
                break
            elif user_input['action'] == 'pause':
                print('Game paused!')
        except json.JSONDecodeError:
            print('Invalid JSON format. Please try again.')
        except ValueError as ve:
            print(ve)
            
if __name__ == '__main__':
    game_loop()