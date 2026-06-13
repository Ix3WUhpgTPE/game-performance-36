import numpy as np

def process_game_data(data):
    cleaned_data = clean_data(data)
    optimized_results = optimize_performance(cleaned_data)
    return optimized_results


def clean_data(data):
    # Filtering out entries with missing or corrupt data
    return [entry for entry in data if validate_entry(entry)]


def validate_entry(entry):
    return all(key in entry for key in ('fps', 'latency', 'score'))


def optimize_performance(data):
    # Utilizing NumPy for performance gains with large data sets
    fps = np.array([entry['fps'] for entry in data])
    latency = np.array([entry['latency'] for entry in data])
    scores = np.array([entry['score'] for entry in data])

    avg_fps = np.mean(fps)
    avg_latency = np.mean(latency)
    total_score = np.sum(scores)

    return {'avg_fps': avg_fps, 'avg_latency': avg_latency, 'total_score': total_score}
