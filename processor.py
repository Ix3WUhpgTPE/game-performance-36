import time
import requests

class NetworkError(Exception):
    pass

class NetworkProcessor:
    def __init__(self, max_retries=5, backoff_factor=2):
        self.max_retries = max_retries
        self.backoff_factor = backoff_factor

    def fetch_data(self, url):
        retries = 0
        while retries < self.max_retries:
            try:
                response = requests.get(url)
                response.raise_for_status()
                return response.json()
            except requests.exceptions.RequestException as e:
                retries += 1
                if retries == self.max_retries:
                    raise NetworkError(f'Failed to fetch data after {retries} attempts') from e
                wait_time = self.backoff_factor ** retries
                print(f'Retrying in {wait_time} seconds...')
                time.sleep(wait_time)

    def process_data(self, url):
        try:
            data = self.fetch_data(url)
            # Perform processing on data
            return data
        except NetworkError as e:
            print(e)
            return None

if __name__ == '__main__':
    processor = NetworkProcessor()
    data = processor.process_data('https://api.example.com/data')
    print(data)