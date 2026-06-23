import random
import json

class GameHandler:
    def __init__(self):
        self.valid_inputs = {"start", "stop", "pause"}

    def validate_input(self, user_input):
        if user_input not in self.valid_inputs:
            raise ValueError(f"Invalid input: {user_input}. Valid options are {self.valid_inputs}.")

    def process_input(self, user_input):
        self.validate_input(user_input)
        response = {"status": "success", "action": user_input}
        print(json.dumps(response))

    def main_loop(self):
        print("Game is starting...")
        while True:
            user_input = input("Enter command (start/stop/pause): ")
            if user_input == "exit":
                print("Exiting game...")
                break
            try:
                self.process_input(user_input)
            except ValueError as e:
                print(e)

if __name__ == '__main__':
    game_handler = GameHandler()
    game_handler.main_loop()