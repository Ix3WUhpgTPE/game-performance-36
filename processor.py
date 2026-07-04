import json

class GameProcessor:
    def __init__(self, game_data):
        self.game_data = game_data

    def process_data(self):
        try:
            self.validate_data(self.game_data)
            processed_data = self._transform_data(self.game_data)
            return json.dumps(processed_data)
        except ValueError as ve:
            return json.dumps({'error': 'Validation Error', 'message': str(ve)})
        except TypeError as te:
            return json.dumps({'error': 'Type Error', 'message': str(te)})
        except Exception as e:
            return json.dumps({'error': 'Unexpected Error', 'message': str(e)})

    def validate_data(self, data):
        if not isinstance(data, dict):
            raise ValueError('Game data must be a dictionary.')
        required_keys = ['name', 'score', 'level']
        for key in required_keys:
            if key not in data:
                raise ValueError(f'Missing required key: {key}')

    def _transform_data(self, data):
        return {
            'game_name': data['name'],
            'game_score': data['score'] * 100,
            'game_level': f'Level {data['level']}'
        }

# Sample usage
if __name__ == '__main__':
    game_info = {'name': 'SuperGame', 'score': 0.85, 'level': 2}
    processor = GameProcessor(game_info)
    print(processor.process_data())