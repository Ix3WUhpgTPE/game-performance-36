import time
import random

def optimize_game_logic(game_state):
    start_time = time.time()
    if not game_state['is_running']:
        return
    for entity in game_state['entities']:
        if entity['type'] == 'player':
            update_player(entity)
        elif entity['type'] == 'enemy':
            update_enemy(entity)
    elapsed_time = time.time() - start_time
    print(f'Optimization took {elapsed_time:.4f} seconds')


def update_player(player):
    player['position'][0] += random.choice([-1, 1])
    player['position'][1] += random.choice([-1, 1])
    player['health'] = max(0, player['health'] - 1)


def update_enemy(enemy):
    enemy['position'][0] = min(max(enemy['position'][0] + random.choice([-1, 0, 1]), 0), 100)
    enemy['position'][1] = min(max(enemy['position'][1] + random.choice([-1, 0, 1]), 0), 100)
    enemy['health'] = max(0, enemy['health'] - 2)