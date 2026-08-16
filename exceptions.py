class GameError(Exception):
    pass

class InitializationError(GameError):
    def __init__(self, message):
        super().__init__(message)
        self.code = 1001

class ConfigurationError(GameError):
    def __init__(self, message):
        super().__init__(message)
        self.code = 1002

class NotFoundError(GameError):
    def __init__(self, message):
        super().__init__(message)
        self.code = 1003

class InvalidInputError(GameError):
    def __init__(self, message):
        super().__init__(message)
        self.code = 1004

class ResourceConflictError(GameError):
    def __init__(self, message):
        super().__init__(message)
        self.code = 1005

# Example of usage
try:
    raise InitializationError('Game failed to initialize.')
except GameError as e:
    print(f'Error: {e}, Code: {e.code}')