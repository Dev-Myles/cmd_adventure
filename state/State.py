"""
This file contain the logic for the keeping track of the state 
of the game. 
"""


class State:
    
    def __init__(self, previous_stage:str, current_stage:str, is_playing: bool) -> None:
        self.current_stage = current_stage
        self.previous_stage = previous_stage
        self.is_playing = False
    
    def is_stage(self):
        return self.current_stage
    
    def is_playing(self):
        return self.is_playing
    
    def set_playing(self, playing:bool):
        self.is_playing = playing
    
    def set_stage(self, selected_stage:str):
        self.previous_stage = self.current_stage
        self.current_stage = selected_stage
        
    def set_player(self, player_info):
        self.player_info = player_info
    
    def is_player_dead(self):
        if self.player_info.health <= 0:
            self.current_stage = "dead"
            self.next_stage = "start"
            return True
        else:
            return False
    
    def display_player_info(self):
        print(self.player_info.values())
        