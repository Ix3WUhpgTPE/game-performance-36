import json
import os

def load_config(file_path, defaults):
    if not os.path.exists(file_path):
        return defaults
    with open(file_path, 'r') as config_file:
        config = json.load(config_file)
        return {**defaults, **config}

if __name__ == '__main__':
    default_settings = {
        'resolution': '1920x1080',
        'fullscreen': True,
        'volume': 75,
        'difficulty': 'normal'
    }
    config_path = 'config.json'
    config = load_config(config_path, default_settings)
    print(config)