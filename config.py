import json
from pathlib import Path

def load_config(file_path: str, defaults: dict) -> dict:
    config_path = Path(file_path)
    if config_path.is_file():
        with open(config_path) as config_file:
            try:
                config = json.load(config_file)
            except json.JSONDecodeError:
                print('Error decoding JSON, using defaults')
                return defaults
    else:
        print('Config file not found, using defaults')
        return defaults

    # Merge defaults with loaded configuration
    return {**defaults, **config}

if __name__ == '__main__':
    default_config = {'setting1': 'value1', 'setting2': 10}
    loaded_config = load_config('config.json', default_config)
    print(loaded_config)