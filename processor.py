import time
import random
import requests

class NetworkError(Exception):
    pass

def retry(max_retries=5, backoff=1.0):
    def decorator(func):
        def wrapper(*args, **kwargs):
            retries = 0
            while retries < max_retries:
                try:
                    return func(*args, **kwargs)
                except (requests.RequestException, NetworkError) as e:
                    retries += 1
                    sleep_time = backoff * (2 ** (retries - 1)) + random.uniform(0, 1)
                    print(f'Attempt {retries} failed: {e}. Retrying in {sleep_time:.2f} seconds...')
                    time.sleep(sleep_time)
            raise NetworkError(f'Failed after {max_retries} attempts')
        return wrapper
    return decorator

@retry(max_retries=3, backoff=2)
def fetch_data(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

# Example usage
if __name__ == '__main__':
    try:
        data = fetch_data('https://api.example.com/data')
        print(data)
    except NetworkError as e:
        print(e)
