"""
This file contains the logic for the creating entities.
"""

class Entity:
    def __init__(self, name:str, health:int, damage:int) -> None:
        self.name = name
        self.health = health
        self.damage = damage
    
    def attack(self):
        return self.damage

    def set_health(self, damage:int):
        self.health -= damage
    
    