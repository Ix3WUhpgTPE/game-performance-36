import time
import random

class GameProcessor:
    def __init__(self):
        self.state = 'initial'
        self.score = 0

    def update_state(self, new_state):
        if new_state in ['running', 'paused', 'stopped']:
            self.state = new_state
        else:
            raise ValueError('Invalid state: ' + new_state)

    def add_score(self, points):
        if points < 0:
            raise ValueError('Points cannot be negative')
        self.score += points

    def reset(self):
        self.state = 'initial'
        self.score = 0

    def random_event(self):
        events = ['bonus', 'minus', 'none']
        event = random.choice(events)
        if event == 'bonus':
            self.add_score(10)
            return 'You gained a bonus!'
        elif event == 'minus':
            self.add_score(-5)
            return 'You lost some points!'
        return 'No event happened.'

    def simulate_game(self, duration):
        self.update_state('running')
        end_time = time.time() + duration
        while time.time() < end_time:
            print(self.random_event())
            time.sleep(1)
        self.update_state('stopped')