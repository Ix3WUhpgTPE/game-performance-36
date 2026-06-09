import json
import os

def load_config(file_path='config.json', defaults=None):
    if defaults is None:
        defaults = {}
    # Load configuration from file if it exists
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            try:
                config = json.load(f)
            except json.JSONDecodeError:
                print('Invalid JSON in configuration file. Using defaults.')
                return defaults
    else:
        print('Configuration file not found. Using defaults.')
        return defaults

    # Merge defaults with loaded config
    return {**defaults, **config}

# Example usage
if __name__ == '__main__':
    default_settings = {
        'volume': 70,
        'resolution': '1920x1080',
        'fullscreen': True,
    }
    config = load_config(defaults=default_settings)
    print('Loaded Configuration:', config)