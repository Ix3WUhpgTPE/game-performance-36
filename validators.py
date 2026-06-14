def validate_input(user_input):
    if not isinstance(user_input, str):
        raise ValueError('Input must be a string')
    if len(user_input) == 0:
        raise ValueError('Input cannot be empty')
    if any(char.isdigit() for char in user_input):
        raise ValueError('Input cannot contain numbers')
    return True

class Game:
    def __init__(self):
        self.running = True

    def main_loop(self):
        while self.running:
            user_input = input('Enter command: ')
            try:
                if validate_input(user_input):
                    self.process_command(user_input)
            except ValueError as e:
                print(f'Invalid input: {e}')

    def process_command(self, command):
        # Placeholder for command processing
        print(f'Processing command: {command}')
