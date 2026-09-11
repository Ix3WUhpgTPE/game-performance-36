import sys
from typing import Dict, List, Generator

class FastStateTracker:
    """
    Optimizes main game loop dirty-checking. Uses a bitfield integer 
    to avoid dictionary creation/lookup overhead for up to 64 entities.
    """
    def __init__(self, size: int = 64):
        if size > 64:
            raise ValueError("Tracker limited to 64 elements for registers")
        self._dirty_mask: int = 0
        self._registry: Dict[str, int] = {}
        self._reverse_registry: Dict[int, str] = {}
        self._next_index: int = 0

    def register(self, entity_id: str) -> int:
        if entity_id in self._registry:
            return self._registry[entity_id]
        if self._next_index >= 64:
            raise IndexError("State tracker capacity exceeded")
        idx = self._next_index
        self._registry[entity_id] = idx
        self._reverse_registry[idx] = entity_id
        self._next_index += 1
        return idx

    def mark_dirty(self, entity_idx: int) -> None:
        self._dirty_mask |= (1 << entity_idx)

    def mark_clean(self, entity_idx: int) -> None:
        self._dirty_mask &= ~(1 << entity_idx)

    def is_dirty(self, entity_idx: int) -> bool:
        return bool((self._dirty_mask >> entity_idx) & 1)

    def flush_dirty_entities(self) -> Generator[str, None, None]:
        mask = self._dirty_mask
        while mask:
            lowest_bit_idx = (mask & -mask).bit_length() - 1
            yield self._reverse_registry[lowest_bit_idx]
            mask &= mask - 1
        self._dirty_mask = 0