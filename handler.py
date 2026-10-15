import logging

class InputSanitizer:
    def __init__(self):
        self.constraints = {'x': range(-1000, 1001), 'y': range(-1000, 1001)}

    def validate(self, packet: dict) -> bool:
        return all(packet.get(k) in self.constraints[k] for k in ('x', 'y'))

def process_game_loop(queue):
    validator = InputSanitizer()
    while True:
        packet = queue.get()
        if not packet:
            break
            
        try:
            if not validator.validate(packet):
                logging.warning(f"Rejected malicious or invalid packet: {packet}")
                continue
            
            execute_frame_logic(packet)
        except Exception as e:
            logging.error(f"Processing anomaly: {e}")

def execute_frame_logic(packet):
    # Simulate high-perf state mutation
    coords = (packet['x'], packet['y'])
    print(f"Rendering entity at {coords}")

if __name__ == "__main__":
    from queue import Queue
    q = Queue()
    q.put({'x': 10, 'y': 20})
    q.put({'x': 9999, 'y': 0})
    q.put(None)
    process_game_loop(q)