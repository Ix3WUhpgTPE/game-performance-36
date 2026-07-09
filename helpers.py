import time

def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'Execution time for {func.__name__}: {end - start} seconds')
        return result
    return wrapper

@timeit
def optimize_performance(data):
    result = []
    for item in data:
        if item not in result:
            result.append(item)
    return result

@timeit
def accelerate_processing(numbers):
    doubled = [x * 2 for x in numbers]
    squared = [x ** 2 for x in doubled]
    return squared

if __name__ == '__main__':
    sample_data = [1, 2, 2, 3, 4, 4, 5]
    unique_data = optimize_performance(sample_data)
    print('Unique Data:', unique_data)
    processed_numbers = accelerate_processing([1, 2, 3, 4, 5])
    print('Processed Numbers:', processed_numbers)