import time

class PerformanceTimer:
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def start(self):
        self.start_time = time.perf_counter()

    def stop(self):
        self.end_time = time.perf_counter()

    def elapsed(self):
        if self.start_time is None or self.end_time is None:
            raise Exception('Timer has not been started or stopped')
        return self.end_time - self.start_time


def optimize_function(func):
    def wrapper(*args, **kwargs):
        timer = PerformanceTimer()
        timer.start()
        result = func(*args, **kwargs)
        timer.stop()
        print(f"Function '{func.__name__}' executed in {timer.elapsed():.4f} seconds")
        return result
    return wrapper


@optimize_function
def expensive_calculation(n):
    total = 0
    for i in range(n):
        total += i ** 2
    return total


if __name__ == '__main__':
    result = expensive_calculation(100000)
    print(result)
