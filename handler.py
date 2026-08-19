import requests
import time
from random import randint

class NetworkOperationError(Exception):
    pass

class NetworkHandler:
    def __init__(self, max_retries=5, backoff_factor=1):
        self.max_retries = max_retries
        self.backoff_factor = backoff_factor

    def retry(self, func, *args, **kwargs):
        for attempt in range(self.max_retries):
            try:
                response = func(*args, **kwargs)
                if response.status_code == 200:
                    return response.json()
                else:
                    raise NetworkOperationError(f"Unexpected status code: {response.status_code}")
            except (requests.exceptions.RequestException, NetworkOperationError) as e:
                print(f"Attempt {attempt + 1} failed: {str(e)}")
                if attempt == self.max_retries - 1:
                    raise
                sleep_time = self.backoff_factor * (2 ** attempt) + randint(0, 1000) / 1000
                time.sleep(sleep_time)

    def get_data(self, url):
        return self.retry(requests.get, url)

# Example usage:
# handler = NetworkHandler()
# data = handler.get_data('https://api.example.com/data')
