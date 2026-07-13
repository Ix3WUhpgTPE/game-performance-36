import random

def roll_dice(sides=6, rolls=1):
    return [random.randint(1, sides) for _ in range(rolls)]


def calculate_health(max_health, damage):
    return max(0, max_health - damage)


def is_valid_move(board, current_position, new_position):
    x, y = current_position
    new_x, new_y = new_position
    return (0 <= new_x < len(board) and
            0 <= new_y < len(board[0]) and
            board[new_x][new_y] == 0)


def print_board(board):
    for row in board:
        print(' '.join(str(cell) for cell in row))


def log_event(event_message):
    with open('game_log.txt', 'a') as log_file:
        log_file.write(event_message + '\n')