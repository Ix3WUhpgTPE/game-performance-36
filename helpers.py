from typing import List, Dict, Any


def calculate_score(points: List[int], multipliers: Dict[str, float]) -> float:
    """
    Calculate the total score based on points and multipliers.

    Args:
        points (List[int]): A list of points scored in different levels.
        multipliers (Dict[str, float]): A dictionary of level names and their respective multipliers.

    Returns:
        float: The calculated total score.
    """
    total_score = 0.0
    for i, point in enumerate(points):
        level_key = f'level_{i + 1}'
        multiplier = multipliers.get(level_key, 1.0)
        total_score += point * multiplier
    return total_score


def get_average_score(scores: List[float]) -> float:
    """
    Calculate the average of a list of scores.

    Args:
        scores (List[float]): A list of scores to average.

    Returns:
        float: The average score, or 0 if the list is empty.
    """
    return sum(scores) / len(scores) if scores else 0.0


def format_score(score: float) -> str:
    """
    Format the score to two decimal places.

    Args:
        score (float): The score to format.

    Returns:
        str: The formatted score as a string.
    """
    return f'{score:.2f}'


# Example usage of the helpers
if __name__ == '__main__':
    scores = [100, 200, 150]
    multipliers = {'level_1': 1.5, 'level_2': 2.0}  
    total = calculate_score(scores, multipliers)
    print(f'Total score: {format_score(total)}')
    average = get_average_score([total])
    print(f'Average score: {format_score(average)}')