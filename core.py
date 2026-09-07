import time

class InputValidator:
    def __init__(self, bounds=(0, 1024)):
        self.bounds = bounds

    def __call__(self, val):
        return self.bounds[0] <= val <= self.bounds[1]

def run_game_loop():
    validator = InputValidator()
    print('Engine heartbeat initialized...')
    
    raw_input_stream = [512, 1200, 100, -50, 800]
    
    for frame_data in raw_input_stream:
        try:
            if not validator(frame_data):
                raise ValueError(f'Input overflow at signal: {frame_data}')
            
            process_physics(frame_data)
        except ValueError as e:
            print(f'Sync error: {e}. Dropping frame to preserve consistency.')
            continue

def process_physics(val):
    # Simulate high-performance compute
    result = (val ** 2) / 0.5
    return result

if __name__ == '__main__':
    run_game_loop()