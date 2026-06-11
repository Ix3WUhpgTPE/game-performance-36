class GamePerformanceError(Exception):
    """Custom exception for game performance issues."""
    def __init__(self, message):
        super().__init__(message)

class InvalidScoreError(GamePerformanceError):
    """Exception raised for invalid score inputs."""
    def __init__(self, score):
        message = f"Invalid score: {score}. Score must be non-negative."
        super().__init__(message)

class ResourceLimitExceeded(GamePerformanceError):
    """Exception raised when resource limits are exceeded."""
    def __init__(self, resource, limit):
        message = f"Resource limit exceeded: {resource} (Limit: {limit})"
        super().__init__(message)

class UnsupportedOperationError(GamePerformanceError):
    """Exception raised for unsupported operations."""
    def __init__(self, operation):
        message = f"Unsupported operation: {operation}"
        super().__init__(message)

class ConfigurationError(GamePerformanceError):
    """Exception raised for configuration errors."""
    def __init__(self, config_key):
        message = f"Configuration error: Missing key {config_key}"
        super().__init__(message)