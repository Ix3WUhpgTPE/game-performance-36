import os

def load_config(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Configuration file '{file_path}' not found.")
    with open(file_path, 'r') as config_file:
        return parse_config(config_file)


def parse_config(config_file):
    config = {}
    for line in config_file:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        key, value = line.split('=', 1)
        config[key.strip()] = value.strip()
    return config


def get_config_value(config, key, default=None):
    return config.get(key, default)


if __name__ == '__main__':
    config_path = 'config.cfg'
    try:
        config = load_config(config_path)
        print("Loaded configuration:", config)
    except Exception as e:
        print(f"Error loading config: {e}")