class InvalidGameStateError(Exception):
    """Raised when the game state is invalid."""
    pass

class PlayerNotFoundError(Exception):
    """Raised when a player is not found in the game."""
    def __init__(self, player_id):
        super().__init__(f'Player with ID {player_id} not found.')
        self.player_id = player_id

class GameOverError(Exception):
    """Raised when an action is attempted after the game is over."""
    def __init__(self):
        super().__init__('Cannot perform action: game is over.')

class InsufficientResourcesError(Exception):
    """Raised when a player tries to perform an action without enough resources."""
    def __init__(self, resource, needed, available):
        super().__init__(f'Insufficient {resource}: needed {needed}, available {available}.')
        self.resource = resource
        self.needed = needed
        self.available = available

class InvalidMoveError(Exception):
    """Raised when a move is invalid in the game context."""
    def __init__(self, move):
        super().__init__(f'Invalid move attempted: {move}.')
        self.move = move
