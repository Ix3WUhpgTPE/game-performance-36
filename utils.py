import json
import os

class ConfigLoader:
    def __init__(self, default_config_path='default_config.json'):
        self.default_config = self.load_config(default_config_path)

    def load_config(self, path):
        if not os.path.exists(path):
            return {}
        with open(path, 'r') as config_file:
            return json.load(config_file)

    def get(self, key, default=None):
        return self.default_config.get(key, default)

    def merge_configs(self, custom_config_path):
        custom_config = self.load_config(custom_config_path)
        merged_config = {**self.default_config, **custom_config}
        return merged_config

    def get_merged_config(self, custom_config_path):
        return self.merge_configs(custom_config_path)

# Example usage:
# loader = ConfigLoader()
# config = loader.get_merged_config('custom_config.json')
# print(config)