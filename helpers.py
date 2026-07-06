from typing import List, Dict, Union


def calculate_fps(frames: int, time_seconds: float) -> float:
    """
    Calculate the frames per second (FPS) based on frames captured
    and the time elapsed.

    :param frames: The number of frames captured.
    :param time_seconds: The time period over which the frames were captured (in seconds).
    :return: The calculated FPS as a float.
    """
    if time_seconds <= 0:
        raise ValueError('Time must be greater than zero')
    return frames / time_seconds


def average_score(scores: List[Union[int, float]]) -> float:
    """
    Calculate the average score from a list of scores.

    :param scores: A list of integer or float scores.
    :return: The average score as a float.
    """
    if not scores:
        raise ValueError('Score list cannot be empty')
    return sum(scores) / len(scores)


def find_highest_score(score_dict: Dict[str, Union[int, float]]) -> str:
    """
    Find the player with the highest score.

    :param score_dict: A dictionary with player names as keys and their scores as values.
    :return: The name of the player with the highest score.
    """
    if not score_dict:
        raise ValueError('Score dictionary cannot be empty')
    return max(score_dict, key=score_dict.get)