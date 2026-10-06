import time
import random

def validate_input(data):
    if not isinstance(data, dict) or 'action' not in data:
        return False
    return data['action'] in {'jump', 'shoot', 'crouch'}

def process_frame(frame_data):
    if not validate_input(frame_data):
        raise ValueError(f"Illegal telemetry: {frame_data}")
    print(f"Executing {frame_data['action']} at timestamp {frame_data.get('ts')}")

def main_loop():
    stream = [
        {'action': 'jump', 'ts': time.time()},
        {'action': 'dance', 'ts': time.time()},
        {'action': 'shoot', 'ts': time.time()}
    ]
    
    for packet in stream:
        try:
            process_frame(packet)
        except ValueError as e:
            print(f"Frame drop: {e}")
            continue

if __name__ == "__main__":
    main_loop()