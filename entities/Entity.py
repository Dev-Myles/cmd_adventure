"""
This file contains the logic for the creating entities.
"""

from graphics.graphics import graphics
import random

class Entity:
    def __init__(self, name:str, health:int, damage:int, class_type: str, accuracy: int) -> None:
        self.name = name
        self.health = health
        self.damage = damage
        self.class_type = class_type
        self.accuracy = accuracy
    
    def attack(self):
        d20_roller = random.randrange(1, 20)
        if d20_roller >= self.accuracy:
            print(f"\n{self.name} attacks and does {self.damage} damage.")
            return self.damage
        else:
            print(f"\n{self.name} attack misses...")
            return 0

    def show_name(self):
        return self.name
    
    def show_health(self):
        if self.health > 0:
            return print(f"{self.name} has {self.health} HP")
        else:
            return print(f"{self.name} has died.")
    
    def set_health(self, damage:int):
        int(damage)
        self.health -= damage
        
    def set_image(self):
        self.graphic = graphics.get(self.class_type)
        
    
    