"""
This file contains all of the logic for stages of the game.
"""
from stages.Stage import Stage
from graphics.graphics import graphics

def stage_list(stage_name: str):
    stages = {
        "title": Stage(graphics.get("title")),
        "road1": Stage(graphics.get("road1")),
        "road2": Stage(graphics.get("road2")),
        "battle_warrior": Stage(graphics.get("battle1")),
        "battle_rouge": Stage(graphics.get("battle2")),
        "warrior": Stage(graphics.get("warrior")),
        "rouge": Stage(graphics.get("rouge")),
        "fight": Stage(graphics.get("fight")),
        "player_win": Stage(graphics.get("player_win")),
        "dragon_win": Stage(graphics.get("died_message"))
        
    }
    
    return stages.get(stage_name)
