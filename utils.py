import time
import random

class NetworkError(Exception):
    pass

def simulate_network_call():
    if random.choice([True, False]):
        raise NetworkError("Network failure occurred")
    return "Success!"

def retry_on_failure(func, retries=5, delay=2):
    attempts = 0
    while attempts < retries:
        try:
            return func()
        except NetworkError as e:
            attempts += 1
            print(f"Attempt {attempts} failed: {e}")
            if attempts < retries:
                time.sleep(delay)
    raise NetworkError("All retries failed")

if __name__ == "__main__":
    try:
        result = retry_on_failure(simulate_network_call)
        print(result)
    except NetworkError:
        print("Final failure, please check network connectivity.")
