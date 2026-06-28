import json

class GameProcessor:
    def __init__(self):
        self.valid_inputs = ['start', 'stop', 'pause', 'resume']

    def validate_input(self, user_input):
        if user_input not in self.valid_inputs:
            raise ValueError(f"Invalid input: {user_input}")

    def main_loop(self):
        while True:
            user_input = input('Enter command (start, stop, pause, resume): ').strip().lower()
            try:
                self.validate_input(user_input)
                self.process_input(user_input)
            except ValueError as e:
                print(e)

    def process_input(self, user_input):
        if user_input == 'start':
            print('Game started!')
        elif user_input == 'stop':
            print('Game stopped!')
        elif user_input == 'pause':
            print('Game paused!')
        elif user_input == 'resume':
            print('Game resumed!')

if __name__ == '__main__':
    processor = GameProcessor()
    processor.main_loop()