import time
import random

def retry_network_operation(func, retries=3, delay=2):
    """Retry a network operation up to a number of retries with a delay.
    """
    for attempt in range(retries):
        try:
            return func()
        except Exception as e:
            print(f'Attempt {attempt + 1} failed: {e}')
            if attempt < retries - 1:
                time.sleep(delay * (2 ** attempt))  # Exponential backoff
    raise Exception('All attempts failed')

# Sample function to simulate a network operation

def sample_network_operation():
    if random.choice([True, False]):  # Randomly succeed or fail
        print('Network operation succeeded')
        return 'Success'
    else:
        raise Exception('Network error')

# Example usage
if __name__ == '__main__':
    try:
        result = retry_network_operation(sample_network_operation)
        print(result)
    except Exception as e:
        print(e)