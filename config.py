import json
import os

class ConfigLoader:
    def __init__(self, default_config_path, custom_config_path=None):
        self.default_config = self.load_config(default_config_path)
        self.custom_config = self.load_config(custom_config_path) if custom_config_path else {}
        self.config = self.merge_configs(self.default_config, self.custom_config)

    def load_config(self, path):
        if not path or not os.path.isfile(path):
            return {}
        with open(path, 'r') as file:
            return json.load(file)

    def merge_configs(self, default, custom):
        config = default.copy()  # Start with default configuration
        config.update(custom)  # Override with custom configuration
        return config

    def get(self, key, default=None):
        return self.config.get(key, default)

# Example usage:
# config_loader = ConfigLoader('default_config.json', 'custom_config.json')
# db_host = config_loader.get('database_host', 'localhost')