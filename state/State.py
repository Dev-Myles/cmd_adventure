"""
This file contain the logic for the keeping track of the state 
of the game. 
"""


class State:
    
    def __init__(self, previous_stage:str, current_stage:str, is_playing: bool) -> None:
        self.current_stage = current_stage
        self.previous_stage = previous_stage
        self.is_playing = False
        self.created_player = False
        self.player_info = {
            "name": "",
            "health":0,
            "damage":0,
            "selected_class": ""
        }
    
    def is_stage(self):
        return self.current_stage
    
    def is_playing(self):
        return self.is_playing
    
    def set_playing(self, playing:bool):
        self.is_playing = playing
    
    def set_stage(self, selected_stage:str):
        self.previous_stage = self.current_stage
        self.current_stage = selected_stage.strip()
        
    def set_player(self, player_info):
        self.player_info = player_info
        self.created_player = True
    
    def is_player_dead(self):
        if self.player_info.health <= 0:
            self.current_stage = "dead"
            self.next_stage = "start"
            return True
        else:
            return False
    
    def reset_player_info(self):
        self.player_info = {
            "name": "",
            "health":0,
            "damage":0,
            "selected_class": ""
        }
    def display_player_name(self):
        name = self.player_info.get("name")
        if len(name) > 0:
            print("Welcome, "+name)
        else:
            return
        
    