import json
import os

class ConfigLoader:
    def __init__(self, default_config, user_config_path=None):
        self.config = default_config
        if user_config_path:
            self.load_user_config(user_config_path)

    def load_user_config(self, user_config_path):
        if os.path.exists(user_config_path):
            with open(user_config_path, 'r') as f:
                user_config = json.load(f)
                self.update_config(user_config)
        else:
            print(f'Warning: {user_config_path} not found. Using default settings.')

    def update_config(self, user_config):
        for key, value in user_config.items():
            if key in self.config:
                self.config[key] = value
            else:
                print(f'Warning: Key {key} not in default config. Skipping.\n')

    def get(self, key):
        return self.config.get(key, None)

# Example of default configuration
DEFAULT_CONFIG = {
    'resolution': '1920x1080',
    'fullscreen': True,
    'volume': 70
}

loader = ConfigLoader(DEFAULT_CONFIG, 'user_config.json')
print(loader.config)  # Display the loaded configuration