import json
import os

def load_config(file_path, default_config):
    if not os.path.exists(file_path):
        return default_config
    with open(file_path, 'r') as file:
        try:
            user_config = json.load(file)
        except json.JSONDecodeError:
            print('Error reading JSON, using defaults')
            return default_config
    return {**default_config, **user_config}

def save_config(file_path, config):
    with open(file_path, 'w') as file:
        json.dump(config, file, indent=4)

if __name__ == '__main__':
    default_config = {'volume': 50, 'resolution': '1920x1080', 'fullscreen': True}
    config_path = 'config.json'
    final_config = load_config(config_path, default_config)
    print(final_config)
    save_config(config_path, final_config)