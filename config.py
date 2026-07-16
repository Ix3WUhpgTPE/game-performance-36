import json
import os

def load_config(file_path='config.json', default=None):
    if default is None:
        default = {'resolution': '1920x1080', 'fullscreen': True, 'volume': 50}
    
    if not os.path.isfile(file_path):
        return default
    
    with open(file_path, 'r') as f:
        try:
            config = json.load(f)
        except json.JSONDecodeError:
            return default
    
    return {**default, **config}

if __name__ == '__main__':
    print(load_config())