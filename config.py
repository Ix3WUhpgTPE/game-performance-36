import os

class Config:
    def __init__(self):
        self.ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
        self.LOAD_PATH = os.path.join(self.ROOT_DIR, 'assets', 'load')
        self.SAVE_PATH = os.path.join(self.ROOT_DIR, 'assets', 'save')
        self.LOG_LEVEL = 'DEBUG'
        self.MAX_PLAYERS = 10
        self.DEFAULT_SETTINGS = {
            'fullscreen': False,
            'resolution': (1920, 1080),
            'volume': 75
        }

    def get_log_file(self):
        return os.path.join(self.ROOT_DIR, 'logs', 'game.log')

    def get_settings(self):
        return self.DEFAULT_SETTINGS

config = Config()

if __name__ == '__main__':
    print(config.get_log_file())
    print(config.get_settings())