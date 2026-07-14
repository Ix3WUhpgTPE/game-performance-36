from typing import List, Dict, Any

class Game:
    def __init__(self, name: str, genre: str, max_players: int) -> None:
        """Initialize the game with name, genre, and max players."""
        self.name = name
        self.genre = genre
        self.max_players = max_players
        self.current_players: List[str] = []

    def add_player(self, player_name: str) -> bool:
        """Add a player to the game if there's space remaining."""
        if len(self.current_players) < self.max_players:
            self.current_players.append(player_name)
            return True
        return False

    def start_game(self) -> Dict[str, Any]:
        """Start the game if enough players have joined."""
        if len(self.current_players) < 2:
            return {'status': 'failed', 'message': 'Not enough players to start the game.'}
        return {'status': 'started', 'players': self.current_players}

    def get_details(self) -> Dict[str, Any]:
        """Return a dictionary with game details."""
        return {
            'name': self.name,
            'genre': self.genre,
            'max_players': self.max_players,
            'current_players': self.current_players,
        }

# Example usage:
game_instance = Game('Epic Quest', 'Adventure', 4)
game_instance.add_player('Player1')
game_instance.add_player('Player2')
result = game_instance.start_game()  
print(result)
print(game_instance.get_details())