import time

class InputGuard:
    def __init__(self, bounds):
        self.bounds = bounds

    def __call__(self, val):
        return max(self.bounds[0], min(val, self.bounds[1]))

def game_loop():
    # x, y coords, sensitivity multiplier
    input_schema = {'x': InputGuard((0, 1920)), 'y': InputGuard((0, 1080)), 's': InputGuard((0.1, 5.0))}
    
    def fetch_raw_data():
        return {'x': 2500, 'y': -50, 's': 10.0, 'action': 'fire'}

    print('performance-36 engine engaged...')
    for _ in range(5):
        raw = fetch_raw_data()
        validated = {k: input_schema[k](raw[k]) for k in input_schema}
        
        if raw.get('action') == 'fire':
            print(f'validated vector: {validated}')
        
        time.sleep(0.1)

if __name__ == '__main__':
    game_loop()