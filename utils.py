import time
import random

def retry_operation(max_retries=5, delay=2):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f'Attempt {attempt + 1} failed: {e}')
                    if attempt < max_retries - 1:
                        time.sleep(delay + random.uniform(0, 1))  # Exponential backoff
                    else:
                        print('All attempts failed')
                        raise
        return wrapper
    return decorator

@retry_operation(max_retries=3, delay=1)
def network_request():
    # Simulating a network operation that may fail
    if random.random() < 0.7:  # 70% chance to fail
        raise Exception('Network error')
    return 'Success!'

if __name__ == '__main__':
    result = network_request()
    print(result)