import time
import random

RETRY_LIMIT = 5
RETRY_DELAY = 2

class NetworkError(Exception):
    pass


def perform_network_operation():
    # Simulate network operation with a chance of failure
    if random.random() < 0.7:
        raise NetworkError("Failed to connect")
    return "Success"


def retry_network_operation():
    attempts = 0
    while attempts < RETRY_LIMIT:
        try:
            result = perform_network_operation()
            return result
        except NetworkError as e:
            attempts += 1
            print(f"Attempt {attempts} failed: {e}")
            if attempts < RETRY_LIMIT:
                time.sleep(RETRY_DELAY)
            else:
                print("All attempts failed.")
                raise
    
# Example usage
# if __name__ == '__main__':
#     try:
#         result = retry_network_operation()
#         print(result)
#     except NetworkError:
#         print("Operation ultimately failed")