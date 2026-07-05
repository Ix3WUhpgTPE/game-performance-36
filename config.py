import json
import os

class ConfigLoader:
    def __init__(self, default_config_path):
        self.default_config_path = default_config_path
        self.config = self.load_defaults()

    def load_defaults(self):
        if not os.path.exists(self.default_config_path):
            raise FileNotFoundError(f"Default config file not found: {self.default_config_path}")
        with open(self.default_config_path, 'r') as config_file:
            return json.load(config_file)

    def update_with_file(self, config_file_path):
        if os.path.exists(config_file_path):
            with open(config_file_path, 'r') as update_file:
                user_config = json.load(update_file)
                self.config.update(user_config)
        else:
            print(f"User config file not found: {config_file_path}")

    def get(self, key, default=None):
        return self.config.get(key, default)

# Example usage:
# loader = ConfigLoader('default_config.json')
# loader.update_with_file('user_config.json')
# print(loader.get('some_setting'))