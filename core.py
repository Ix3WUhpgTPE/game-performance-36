import sys

def validate_input(frame_data):
    required = {'player_id': int, 'action': str, 'timestamp': float}
    if not isinstance(frame_data, dict):
        return False
    return all(isinstance(frame_data.get(k), t) for k, t in required.items())

def main_loop(input_stream):
    try:
        for packet in input_stream:
            if not validate_input(packet):
                print(f"dropping malformed frame: {packet}")
                continue
            process_physics(packet)
    except KeyboardInterrupt:
        print("shutting down performance loop")

def process_physics(data):
    # simulates high performance game state update
    print(f"processing {data['action']} for {data['player_id']}")

if __name__ == "__main__":
    # simulation of input queue
    sample_packets = [
        {'player_id': 1, 'action': 'move', 'timestamp': 100.5},
        {'player_id': 'error', 'action': 'jump', 'timestamp': 101.0},
        {'player_id': 2, 'action': 'shoot', 'timestamp': 102.3}
    ]
    main_loop(sample_packets)