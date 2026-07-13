class InvalidInputError(Exception):
    """Exception raised for invalid inputs."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


def validate_input(user_input):
    if not isinstance(user_input, str):
        raise InvalidInputError('Input must be a string')
    if len(user_input) == 0:
        raise InvalidInputError('Input cannot be empty')
    if not user_input.isalnum():
        raise InvalidInputError('Input must be alphanumeric')


if __name__ == '__main__':
    while True:
        try:
            user_input = input('Enter your command: ')
            validate_input(user_input)
            print(f'Valid input received: {user_input}')
        except InvalidInputError as e:
            print(f'Error: {e}')
        except KeyboardInterrupt:
            print('\nExiting...')
            break
        except Exception as e:
            print(f'Unexpected error: {e}')