import time
import random

class NetworkError(Exception):
    pass

def retry_on_failure(max_retries=3, wait_time=2):
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_retries:
                try:
                    return func(*args, **kwargs)
                except NetworkError:
                    attempts += 1
                    if attempts == max_retries:
                        raise
                    print(f'Attempt {attempts} failed, retrying in {wait_time} seconds...')
                    time.sleep(wait_time)
        return wrapper
    return decorator

@retry_on_failure(max_retries=5, wait_time=1)
def fetch_data_from_network():
    if random.choice([True, False]):
        raise NetworkError('Failed to fetch data')
    return "Data retrieved!"

if __name__ == '__main__':
    try:
        result = fetch_data_from_network()
        print(result)
    except NetworkError:
        print('All retries failed.')