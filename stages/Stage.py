"""
This file contains the logic for creating the stages for
the game.
"""
from system.System import System


class Stage:
    def __init__(self, stage_graphic:str) -> None:
        self.stage_graphic = stage_graphic
    
    def display_stage(self):
        System.clear_screen()
        return print(self.stage_graphic)
        
    
    