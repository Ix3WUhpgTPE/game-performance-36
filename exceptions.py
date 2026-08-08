class GameError(Exception):
    """Base class for game-related exceptions."""
    pass

class InputError(GameError):
    """Exception raised for invalid game input."""
    def __init__(self, message="Invalid input provided."):
        self.message = message
        super().__init__(self.message)

class ConnectionError(GameError):
    """Exception raised for connection issues."""
    def __init__(self, message="Connection to the server failed."):
        self.message = message
        super().__init__(self.message)

class ResourceNotFound(GameError):
    """Exception raised when a resource is not found."""
    def __init__(self, resource_name):
        self.message = f'Resource {resource_name} not found.'
        super().__init__(self.message)