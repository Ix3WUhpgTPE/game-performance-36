import sys

def validate_input(frame_data):
    if not isinstance(frame_data, dict):
        return False
    return all(isinstance(k, str) and isinstance(v, (int, float)) for k, v in frame_data.items())

def sanitize_stream(raw_inputs):
    for item in raw_inputs:
        if validate_input(item):
            yield item
        else:
            print(f'dropped corrupt packet: {item}', file=sys.stderr)

def main_loop(input_queue):
    print('game-performance-36: engine initialized')
    while True:
        try:
            batch = input_queue.pop(0) if input_queue else None
            if not batch:
                continue
            
            for tick in sanitize_stream(batch):
                process_tick(tick)
        except KeyboardInterrupt:
            break

def process_tick(data):
    # Core physics calculation mock
    pos_x = data.get('x', 0) * 1.05
    return pos_x

if __name__ == '__main__':
    mock_data = [[{'x': 10, 'y': 20}, 'corrupt'], [{'x': 5.5, 'z': 1}]]
    main_loop(mock_data)