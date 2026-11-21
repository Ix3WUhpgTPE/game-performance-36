import json
import os
from typing import Any, Dict

class ConfigLoader:
    """Dynamic dictionary proxy for game configurations."""
    def __init__(self, defaults: Dict[str, Any], path: str = 'settings.json'):
        self.path = path
        self.data = defaults.copy()
        self._load()

    def _load(self) -> None:
        if os.path.exists(self.path):
            with open(self.path, 'r') as f:
                try:
                    user_data = json.load(f)
                    self.data.update(user_data)
                except json.JSONDecodeError:
                    pass

    def __getattr__(self, name: str) -> Any:
        return self.data.get(name)

    def __setattr__(self, name: str, value: Any) -> None:
        if name in ('path', 'data'):
            super().__setattr__(name, value)
        else:
            self.data[name] = value
            self._save()

    def _save(self) -> None:
        with open(self.path, 'w') as f:
            json.dump(self.data, f, indent=4)

    def __repr__(self) -> str:
        return f"Config({self.data})"