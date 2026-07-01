class GameError(Exception):
    pass

class Player:
    def __init__(self, name, health=100):
        if not name:
            raise GameError('Player name cannot be empty')
        self.name = name
        self.health = health

class Game:
    def __init__(self):
        self.players = []

    def add_player(self, player_name):
        try:
            new_player = Player(player_name)
            self.players.append(new_player)
        except GameError as e:
            print(f'Error adding player: {e}')

    def start_game(self):
        if not self.players:
            raise GameError('Cannot start game with no players')
        print('Game has started!')

    def player_action(self, player_name, action):
        player = next((p for p in self.players if p.name == player_name), None)
        if not player:
            print(f'Player {player_name} not found')
            return
        if action not in ['attack', 'defend']:
            print('Invalid action!')
            return
        print(f'{player_name} performs action: {action}')

# Example of usage
if __name__ == '__main__':
    game = Game()
    game.add_player('Alice')
    game.add_player('')  # This will raise an error
    game.start_game()
    game.player_action('Alice', 'attack')
    game.player_action('Bob', 'defend')  # Player not found
    game.player_action('Alice', 'fly')  # Invalid action