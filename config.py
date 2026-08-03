import json
import os

class ConfigLoader:
    def __init__(self, default_config):
        self.default_config = default_config
        self.loaded_config = self.default_config.copy()

    def load_from_file(self, filepath):
        if os.path.exists(filepath):
            with open(filepath, 'r') as file:
                file_config = json.load(file)
                self.loaded_config.update(file_config)

    def get(self, key, default=None):
        return self.loaded_config.get(key, default)

# Default configuration
DEFAULT_CONFIG = {
    'volume': 70,
    'resolution': '1920x1080',
    'fullscreen': True
}

# Usage
if __name__ == '__main__':
    config_loader = ConfigLoader(DEFAULT_CONFIG)
    config_loader.load_from_file('config.json')
    volume = config_loader.get('volume')
    resolution = config_loader.get('resolution')
    print(f'Volume: {volume}, Resolution: {resolution}')