from typing import List, Dict, Any


def calculate_frame_time(frames: List[float]) -> float:
    """
    Calculate the average frame time from provided frame times.

    Args:
        frames (List[float]): A list of frame times in seconds.

    Returns:
        float: The average frame time.
    """
    return sum(frames) / len(frames) if frames else 0.0


def format_game_stats(stats: Dict[str, Any]) -> str:
    """
    Convert game statistics to a formatted string.

    Args:
        stats (Dict[str, Any]): Dictionary containing game stats.

    Returns:
        str: Formatted string of the game stats.
    """
    return '\n'.join(f'{key}: {value}' for key, value in stats.items())


def load_configuration(file_path: str) -> Dict[str, Any]:
    """
    Load game configuration from a JSON file.

    Args:
        file_path (str): The path to the configuration JSON file.

    Returns:
        Dict[str, Any]: The loaded configuration.
    """
    import json
    with open(file_path, 'r') as file:
        return json.load(file)


def is_high_performance(config: Dict[str, Any]) -> bool:
    """
    Determine if the game is set to high performance.

    Args:
        config (Dict[str, Any]): Game configuration.

    Returns:
        bool: True if high performance, False otherwise.
    """
    return config.get('performance_mode', 'normal') == 'high'