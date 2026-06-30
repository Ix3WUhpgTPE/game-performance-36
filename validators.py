import json

class Validator:
    def __init__(self, schema):
        self.schema = schema

    def validate(self, data):
        for key, value in self.schema.items():
            if key not in data:
                raise ValueError(f"Missing key: {key}")
            if not isinstance(data[key], value):
                raise TypeError(f"Invalid type for {key}: expected {value.__name__}, got {type(data[key]).__name__}")
        return True

    def validate_json(self, json_string):
        data = json.loads(json_string)
        return self.validate(data)

if __name__ == '__main__':
    # Sample schema definition
    schema = {'player_name': str, 'score': int, 'level': int}
    v = Validator(schema)
    sample_data = {'player_name': 'Gamer123', 'score': 1500, 'level': 5}
    print(v.validate(sample_data))  # Should print True  
    sample_json = '{"player_name": "Gamer123", "score": 1500, "level": 5}'
    print(v.validate_json(sample_json))  # Should print True
