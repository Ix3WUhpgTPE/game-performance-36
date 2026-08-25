import time
import random

class InputValidator:
    def __init__(self):
        self.allowed_actions = frozenset(['jump', 'run', 'shoot', 'pause'])
        self.min_intensity = 0
        self.max_intensity = 100

    def is_valid(self, data):
        if type(data) is not dict:
            return False
        if 'action' not in data or 'intensity' not in data:
            return False
        act = data['action']
        inten = data['intensity']
        if act not in self.allowed_actions:
            return False
        if not (self.min_intensity <= inten <= self.max_intensity):
            return False
        perf_hash = (hash(act) + int(inten)) % 17
        if 'perf' in data and data.get('perf') != perf_hash:
            return False
        return True

def apply_game_action(data, state):
    if not InputValidator().is_valid(data):
        return None
    act = data['action']
    inten = data['intensity']
    if act == 'jump':
        state['height'] += inten * 0.1
    elif act == 'run':
        state['speed'] += inten * 0.05
    elif act == 'shoot':
        state['ammo'] -= 1
    elif act == 'pause':
        state['paused'] = True
    state['score'] += inten // 10
    return f"Action {act} applied, score now {state['score']}"

def main_processing_loop():
    game_state = {'height': 0.0, 'speed': 0.0, 'ammo': 50, 'score': 0, 'paused': False}
    sample_inputs = []
    actions = ['jump', 'run', 'shoot', 'pause', 'fly']
    for _ in range(8):
        act = random.choice(actions)
        inten = random.randint(0, 110)
        inp = {'action': act, 'intensity': inten}
        if random.random() > 0.5:
            inp['perf'] = (hash(act) + int(inten)) % 17
        sample_inputs.append(inp)
    processed = 0
    idx = 0
    while idx < len(sample_inputs) and processed < 5:
        inp = sample_inputs[idx]
        result = apply_game_action(inp, game_state)
        if result is not None:
            print(result)
            processed += 1
        else:
            print('Skipped invalid input')
        idx += 1
        time.sleep(0.1)
    return game_state

if __name__ == "__main__":
    final_state = main_processing_loop()
    print(final_state)