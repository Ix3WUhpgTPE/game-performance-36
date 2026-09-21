from dataclasses import dataclass
from typing import Any, Dict

@dataclass(frozen=True)
class FrameInput:
    frame_id: int
    payload: Dict[str, float]

def validate_stream(raw_data: Any) -> FrameInput:
    if not isinstance(raw_data, dict) or 'id' not in raw_data:
        raise ValueError('Invalid frame schema')
    if not all(isinstance(v, (int, float)) for v in raw_data.get('metrics', {}).values()):
        raise TypeError('Metric contamination detected')
    return FrameInput(int(raw_data['id']), raw_data.get('metrics', {}))

def process_game_loop(buffer: list):
    processed_frames = []
    for entry in buffer:
        try:
            validated = validate_stream(entry)
            # Injecting latency spike protection
            if validated.payload.get('latency', 0) > 100:
                continue
            processed_frames.append(validated)
        except (ValueError, TypeError) as e:
            print(f'Frame corruption intercepted: {e}')
            continue
    return processed_frames