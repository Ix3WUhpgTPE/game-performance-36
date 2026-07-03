import json
import os

class ConfigLoader:
    def __init__(self, default_config_path):
        self.default_config_path = default_config_path
        self.config = self.load_defaults()  

    def load_defaults(self):
        if os.path.exists(self.default_config_path):
            with open(self.default_config_path, 'r') as f:
                return json.load(f)
        return {}

    def update_with_env(self):
        for key, value in os.environ.items():
            if key in self.config:
                self.config[key] = value

    def get(self, key, default=None):
        return self.config.get(key, default)

    def save(self, file_path):
        with open(file_path, 'w') as f:
            json.dump(self.config, f, indent=4)

# Usage example
# config_loader = ConfigLoader('default_config.json')
# config_loader.update_with_env()