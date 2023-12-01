"""
This file contains the logic for creating the stages for
the game.
"""
class Stage:
    def __init__(self, stage_graphic:str) -> None:
        self.stage_graphic = stage_graphic
    
    def display_stage(self):
        return print(self.stage_graphic)
        
    
    