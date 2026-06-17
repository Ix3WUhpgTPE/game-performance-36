from typing import List, Optional


def calculate_average(scores: List[Optional[int]]) -> float:
    """
    Calculate the average of a list of scores.
    Ignores None values in the list.

    Parameters:
    scores (List[Optional[int]]): List of scores which may include None.

    Returns:
    float: The average score, returns 0.0 if no valid scores are present.
    """
    valid_scores = [score for score in scores if score is not None]
    return sum(valid_scores) / len(valid_scores) if valid_scores else 0.0


def format_player_name(name: str) -> str:
    """
    Format the player's name by capitalizing each word.
    
    Parameters:
    name (str): The player's name to format.

    Returns:
    str: The formatted name.
    """
    return ' '.join(word.capitalize() for word in name.split())


def generate_player_id(length: int = 8) -> str:
    """
    Generate a random player ID consisting of letters and digits.
    
    Parameters:
    length (int): The length of the player ID. Defaults to 8.

    Returns:
    str: A random string of the specified length.
    """
    import random
    import string
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))
