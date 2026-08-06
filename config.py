from typing import Dict, Any

class GameConfig:
    """
    Class to handle game configurations.
    """
    def __init__(self, config: Dict[str, Any]) -> None:
        """Initialize with game configuration dictionary."""
        self.config = config

    def get_setting(self, key: str, default: Any = None) -> Any:
        """Get a setting from the configuration, returns default if not found."""
        return self.config.get(key, default)

    def set_setting(self, key: str, value: Any) -> None:
        """Set a configuration setting to a new value."""
        self.config[key] = value

    def load_from_file(self, filepath: str) -> None:
        """Load configuration from a JSON file."""
        import json
        with open(filepath, 'r') as file:
            self.config.update(json.load(file))

    def save_to_file(self, filepath: str) -> None:
        """Save the current configuration to a JSON file."""
        import json
        with open(filepath, 'w') as file:
            json.dump(self.config, file, indent=4)