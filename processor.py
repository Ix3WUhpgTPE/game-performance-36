import random

class GameDataProcessor:
    def __init__(self, data):
        self.data = data

    def process(self):
        try:
            if not isinstance(self.data, list):
                raise ValueError('Data should be a list')
            if len(self.data) == 0:
                raise ValueError('Data list cannot be empty')

            processed_data = []
            for item in self.data:
                self.validate_item(item)
                processed_data.append(self.transform_item(item))
            return processed_data

        except ValueError as ve:
            print(f'ValueError: {ve}')
        except Exception as e:
            print(f'Unexpected error: {e}')

    def validate_item(self, item):
        if not isinstance(item, int):
            raise TypeError('Each item must be an integer')

    def transform_item(self, item):
        # Simulate some processing on the item
        return item ** 2 + random.randint(1, 10)

# Example usage:
# processor = GameDataProcessor([1, 2, 3])
# result = processor.process()
# print(result)