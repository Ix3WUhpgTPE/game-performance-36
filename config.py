from pathlib import Path

class Config:
    """Configuration settings for the game."""
    def __init__(self, game_name: str, version: str, base_path: Path) -> None:
        """Initialize config with game details.

        Args:
            game_name (str): Name of the game.
            version (str): Version of the game.
            base_path (Path): Base path for configuration files.
        """
        self.game_name = game_name
        self.version = version
        self.base_path = base_path
        self.settings_path = base_path / 'settings.json'

    def load_settings(self) -> dict:
        """Load the game settings from a JSON file.

        Returns:
            dict: Game settings loaded from the file.
        """
        import json
        if self.settings_path.exists():
            with open(self.settings_path) as f:
                return json.load(f)
        return {}

    def save_settings(self, settings: dict) -> None:
        """Save the game settings to a JSON file.

        Args:
            settings (dict): Game settings to save.
        """
        import json
        with open(self.settings_path, 'w') as f:
            json.dump(settings, f, indent=4)