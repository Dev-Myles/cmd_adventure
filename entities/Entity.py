"""
This file contains the logic for the creating entities.
"""

from graphics.graphics import graphics

class Entity:
    def __init__(self, name:str, health:int, damage:int, class_type: str) -> None:
        self.name = name
        self.health = health
        self.damage = damage
        self.class_type = class_type
    
    def attack(self):
        return self.damage

    def show_name(self):
        return self.name
    
    def set_health(self, damage:int):
        self.health -= damage
        
    def set_image(self):
        self.graphic = graphics.get(self.class_type)
        
    
    