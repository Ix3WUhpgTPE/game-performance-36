import random
import time


def wait_for(seconds):
    time.sleep(seconds)


def random_choice(choices):
    return random.choice(choices)


def calculate_avg(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def time_function(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function '{func.__name__}' executed in {{end_time - start_time:.4f}} seconds")
        return result
    return wrapper


def format_score(score):
    return f"Score: {score:.2f}"


def shuffle_list(lst):
    random.shuffle(lst)
    return lst
