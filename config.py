import os

class Config:
    def __init__(self):
        self.debug = self.get_env_variable('DEBUG', 'False') == 'True'
        self.database_url = self.get_env_variable('DATABASE_URL', 'sqlite:///default.db')
        self.api_key = self.get_env_variable('API_KEY')
        self.log_level = self.get_env_variable('LOG_LEVEL', 'INFO')

    def get_env_variable(self, var_name, default_value=None):
        return os.environ.get(var_name, default_value)

config = Config()