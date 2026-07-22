import time
import random
import requests

def retry_request(url, max_retries=5, backoff_factor=1):
    for attempt in range(max_retries):
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            wait = backoff_factor * (2 ** attempt) + random.uniform(0, 1)
            print(f"Attempt {attempt + 1} failed: {e}, retrying in {wait:.2f} seconds...")
            time.sleep(wait)
            
    raise Exception(f"All {max_retries} attempts failed.")

# Example usage
if __name__ == '__main__':
    result = retry_request('https://api.example.com/data')
    print(result)