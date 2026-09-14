class PerformanceThresholdError(Exception):
    """Raised when frame timing exceeds latency budget."""
    def __init__(self, latency, threshold):
        self.message = f"Latency {latency}ms exceeded budget of {threshold}ms"
        super().__init__(self.message)

class ResourceExhaustionError(Exception):
    """Raised when heap or GPU memory hits critical levels."""
    def __init__(self, resource, usage):
        self.message = f"Critical failure: {resource} usage at {usage}%"
        super().__init__(self.message)

class DependencyInjectionError(Exception):
    """Custom error for malformed engine plugin bindings."""
    pass

def raise_if_lagging(frame_time, threshold=16.6):
    if frame_time > threshold:
        raise PerformanceThresholdError(frame_time, threshold)

class EngineErrorHandler:
    @staticmethod
    def handle_critical(err):
        # Log and initiate immediate state save
        print(f"[CRITICAL] {err.__class__.__name__}: {err}")
        return True