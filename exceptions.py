class GameError(Exception):
    def __init__(self, message, code):
        super().__init__(message)
        self.code = code

class ValidationError(GameError):
    pass

class ConnectionError(GameError):
    pass

class ResourceNotFoundError(GameError):
    pass

def handle_game_exception(e):
    if isinstance(e, ValidationError):
        return {'status': 'error', 'message': str(e), 'code': e.code}
    elif isinstance(e, ConnectionError):
        return {'status': 'error', 'message': 'Failed to connect, please try again.', 'code': e.code}
    elif isinstance(e, ResourceNotFoundError):
        return {'status': 'error', 'message': 'Requested resource not found.', 'code': e.code}
    return {'status': 'error', 'message': 'An unexpected error occurred.', 'code': 500}
