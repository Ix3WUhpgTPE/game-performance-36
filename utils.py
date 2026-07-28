import time
import random
import requests

def retry_network_operation(max_retries=5, backoff_factor=1.0):
    def decorator(func):
        def wrapper(*args, **kwargs):
            retries = 0
            while retries < max_retries:
                try:
                    return func(*args, **kwargs)
                except requests.ConnectionError as e:
                    retries += 1
                    wait_time = backoff_factor * (2 ** (retries - 1)) + random.uniform(0, 1)
                    print(f"Retry {retries}/{max_retries}, waiting {wait_time:.2f} seconds...")
                    time.sleep(wait_time)
            raise Exception(f"Network operation failed after {max_retries} retries")
        return wrapper
    return decorator

@retry_network_operation(max_retries=3)
def fetch_data(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()
