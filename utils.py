import time
import random

class NetworkError(Exception):
    pass

def network_operation():
    if random.choice([True, False]):
        raise NetworkError("Simulated network failure")
    return "Network operation successful"

def retry_operation(operation, retries=3, delay=2):
    for attempt in range(retries):
        try:
            result = operation()
            return result
        except NetworkError as e:
            print(f"Attempt {attempt + 1}: {e}")
            if attempt < retries - 1:
                time.sleep(delay)
    return "Operation failed after retries"

if __name__ == '__main__':
    print(retry_operation(network_operation))
