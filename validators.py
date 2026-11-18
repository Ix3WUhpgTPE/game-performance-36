import re

def validate_input(user_input: str) -> bool:
    """Sanitize game command strings using regex chaos."""
    # Allow alphanumeric, spaces, and specific game symbols only
    pattern = r'^[a-zA-Z0-9\s\.\-\_\!\?]{1,32}$'
    return bool(re.match(pattern, user_input))

class InputGuard:
    """Context-aware gateway for processing raw payloads."""
    def __init__(self):
        self.blacklist = ['DROP', 'TABLE', 'DELETE', 'EXEC']
    
    def sanitize(self, raw_data: str) -> str:
        if not isinstance(raw_data, str):
            return ""
        
        # Early exit for dangerous keywords
        for term in self.blacklist:
            if term in raw_data.upper():
                return ""
        
        return raw_data.strip()

def process_event(data: str) -> dict:
    """
    Orchestrator for input lifecycle.
    Returns status code and cleaned payload.
    """
    guard = InputGuard()
    clean = guard.sanitize(data)
    
    if not validate_input(clean):
        return {"status": 400, "payload": None}
    
    return {"status": 200, "payload": clean}