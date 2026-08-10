class GameError(Exception):
    """Base class for game-related errors."""
    pass

class PlayerError(GameError):
    """Raised when there is an issue with the player."""
    def __init__(self, message, player_id):
        super().__init__(message)
        self.player_id = player_id
        
class GameStateError(GameError):
    """Raised when there is a state inconsistency in the game."""
    def __init__(self, message, state):
        super().__init__(message)
        self.state = state
        
def handle_game_error(error):
    if isinstance(error, PlayerError):
        return {"error": "Player issue", "player_id": error.player_id, "message": str(error)}
    elif isinstance(error, GameStateError):
        return {"error": "Game state issue", "state": error.state, "message": str(error)}
    return {"error": "General game error", "message": str(error)}

# Usage example:
if __name__ == '__main__':
    try:
        raise PlayerError("Player not found", player_id=42)
    except GameError as e:
        error_info = handle_game_error(e)
        print(error_info)