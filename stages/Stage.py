"""
This file contains the logic for creating the stages for
the game.
"""


class Stage:
    def __init__(self, stage_name:str) -> None:
        self.stage_name = stage_name
    
    def display_stage(self):
        print(self.stage_name)
        
    
    