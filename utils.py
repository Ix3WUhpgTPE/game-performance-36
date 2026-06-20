import time
import random
import requests

def retry_request(url, retries=3, delay=2):
    for attempt in range(retries):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as err:
            print(f"HTTP error on attempt {attempt + 1}: {err}")
        except requests.exceptions.RequestException as err:
            print(f"Request exception on attempt {attempt + 1}: {err}")
        time.sleep(delay)
    print("All retry attempts failed.")
    return None

# Mocking a network call for demo
if __name__ == '__main__':
    url = 'https://api.example.com/data'
    result = retry_request(url)
    print(result if result else 'Failed to fetch data.')