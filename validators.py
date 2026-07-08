def validate_player_stats(player_stats):
    if not isinstance(player_stats, dict):
        raise ValueError("Player stats must be a dictionary")
    required_keys = ['level', 'experience', 'health']
    for key in required_keys:
        if key not in player_stats:
            raise ValueError(f"Missing required key: {key}")
        if not isinstance(player_stats[key], (int, float)):
            raise TypeError(f"{key} must be an int or float")
        if key == 'level' and player_stats[key] < 1:
            raise ValueError("Level must be greater than 0")
        if key == 'experience' and player_stats[key] < 0:
            raise ValueError("Experience cannot be negative")
        if key == 'health' and player_stats[key] < 0:
            raise ValueError("Health cannot be negative")
    return True

# Example Usage:
if __name__ == '__main__':
    stats = {'level': 5, 'experience': 1500, 'health': 100}
    try:
        validate_player_stats(stats)
        print("Player stats are valid.")
    except Exception as e:
        print(e)