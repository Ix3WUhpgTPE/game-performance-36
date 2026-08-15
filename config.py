import json
import os

class ConfigLoader:
    def __init__(self, default_config, config_file=None):
        self.default_config = default_config
        self.config_file = config_file
        self.config = self.load_config()  

    def load_config(self):
        config = self.default_config.copy()
        if self.config_file and os.path.exists(self.config_file):
            with open(self.config_file, 'r') as f:
                file_config = json.load(f)
                config.update(file_config)
        return config  

    def get(self, key, default=None):
        return self.config.get(key, default)

    def set(self, key, value):
        self.config[key] = value

    def save(self):
        if self.config_file:
            with open(self.config_file, 'w') as f:
                json.dump(self.config, f, indent=4)

# Example usage:
# default_config = {'resolution': '1920x1080', 'volume': 75}
# loader = ConfigLoader(default_config, 'config.json')
# print(loader.get('resolution'))
# loader.set('volume', 85)
# loader.save()