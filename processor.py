import random
import json
import sys

def validate_input(user_input):
    if not user_input.isdigit():
        raise ValueError('Input must be a number.')
    number = int(user_input)
    if not (1 <= number <= 100):
        raise ValueError('Input must be between 1 and 100.')
    return number

def process_user_input(user_input):
    try:
        valid_number = validate_input(user_input)
        print(f'Processing number: {valid_number}')
        # Simulating some processing logic
        result = random.randint(1, 100) + valid_number
        return {'result': result}
    except ValueError as e:
        return {'error': str(e)}

def main_loop():
    while True:
        user_input = input('Enter a number (1-100 or q to quit): ')
        if user_input.lower() == 'q':
            print('Exiting the program.')
            break
        output = process_user_input(user_input)
        print(json.dumps(output))

if __name__ == '__main__':
    main_loop()