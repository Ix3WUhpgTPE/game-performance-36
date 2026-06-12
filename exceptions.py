class GameError(Exception):
    """Base class for game-related exceptions."""
    def __init__(self, message):
        super().__init__(message)
        self.message = message

class InputError(GameError):
    """Raised for errors in user input."""
    pass

class ConnectionError(GameError):
    """Raised when a game connection fails."""
    pass

class ResourceError(GameError):
    """Raised for missing or invalid game resources."""
    def __init__(self, resource, message='Resource not found or invalid.'):
        super().__init__(f"{message}: {resource}")
        self.resource = resource

class LevelError(GameError):
    """Raised for invalid game level operations."""
    def __init__(self, level, message='Invalid level operation.'):
        super().__init__(f"{message}: {level}")
        self.level = level

# Example use of custom exceptions
try:
    raise InputError('Invalid move detected')
except InputError as e:
    print(e)

try:
    raise ResourceError('sword', 'Item is not available')
except ResourceError as e:
    print(e)

try:
    raise LevelError(5, 'Level does not exist')
except LevelError as e:
    print(e)