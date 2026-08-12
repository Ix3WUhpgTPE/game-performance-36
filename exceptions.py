class GameError(Exception):
    pass

class ResourceNotFound(GameError):
    def __init__(self, resource_name):
        self.resource_name = resource_name
        super().__init__(f'Resource not found: {resource_name}')

class InvalidAction(GameError):
    def __init__(self, action):
        self.action = action
        super().__init__(f'Invalid action attempted: {action}')

class GameStateError(GameError):
    def __init__(self, state):
        self.state = state
        super().__init__(f'Game state error: {state}')

# Custom error handling for game instances

def handle_exception(exception):
    if isinstance(exception, ResourceNotFound):
        print(f'Error: {exception}')
    elif isinstance(exception, InvalidAction):
        print(f'Error: {exception}')
    elif isinstance(exception, GameStateError):
        print(f'Error: {exception}')
    else:
        print(f'An unknown error occurred: {exception}')

# Example usage
if __name__ == '__main__':
    try:
        raise ResourceNotFound('Weapon')
    except GameError as e:
        handle_exception(e)