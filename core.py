import random

class GameCharacter:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
        self.is_alive = True

    def take_damage(self, damage):
        if damage < 0:
            raise ValueError('Damage cannot be negative')
        self.health -= damage
        if self.health <= 0:
            self.is_alive = False
            self.health = 0
            print(f'{self.name} has been defeated!')

    def attack_enemy(self, enemy):
        if not isinstance(enemy, GameCharacter):
            raise TypeError('Enemy must be a GameCharacter instance')
        if not self.is_alive:
            raise RuntimeError(f'{self.name} cannot attack as they are defeated')
        print(f'{self.name} attacks {enemy.name} for {self.attack} damage!')
        enemy.take_damage(self.attack)

    def heal(self, amount):
        if amount < 0:
            raise ValueError('Healing amount cannot be negative')
        self.health += amount
        print(f'{self.name} heals for {amount} points! Current health: {self.health}')

# Example usage

try:
    hero = GameCharacter('Hero', 100, 20)
    villain = GameCharacter('Villain', 80, 15)
    hero.attack_enemy(villain)
    villain.attack_enemy(hero)
    hero.heal(10)
except (ValueError, TypeError, RuntimeError) as e:
    print(f'Error: {e}')