class ValidationError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


def validate_input(user_input):
    if not isinstance(user_input, str):
        raise ValidationError('Input must be a string')
    if not user_input:
        raise ValidationError('Input cannot be empty')
    if len(user_input) > 50:
        raise ValidationError('Input cannot exceed 50 characters')


def main_loop():
    while True:
        user_input = input('Enter a command: ')
        try:
            validate_input(user_input)
            print(f'Processed input: {user_input}')
        except ValidationError as e:
            print(f'Error: {e.message}')
        except Exception as e:
            print(f'Unexpected error: {str(e)}')


if __name__ == '__main__':
    main_loop()