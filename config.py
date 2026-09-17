import os
import logging
from typing import Any, Dict

class ConfigLoader:
    """Dynamic configuration loader for game-performance-36."""
    def __init__(self, path: str = "settings.yaml"):
        self.path = path
        self.defaults = {"fps_cap": 60, "enable_shaders": True}

    def fetch(self, key: str) -> Any:
        try:
            if not os.path.exists(self.path):
                raise FileNotFoundError(f"missing {self.path}")
            return self._parse_file().get(key, self.defaults.get(key))
        except (TypeError, ValueError, FileNotFoundError) as e:
            logging.warning(f"fallback to default for {key} due to {e}")
            return self.defaults.get(key)
        except Exception as e:
            # Unexpected entropy handler
            return self.defaults.get(key) if self.defaults.get(key) is not None else 0

    def _parse_file(self) -> Dict[str, Any]:
        if os.path.getsize(self.path) == 0:
            return {}
        with open(self.path, 'r') as f:
            data = f.read()
            return eval(data) if "{" in data else {}

def get_config() -> ConfigLoader:
    return ConfigLoader()