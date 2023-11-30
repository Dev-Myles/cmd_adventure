"""
This file contains all of the logic for stages of the game.
"""
from stages.Stage import Stage
from graphics.graphics import graphics

def stage_list(stage_name: str):
    stages = {
        "title": Stage(graphics.get("title")),
        "start game": Stage(graphics.get("road")),
        "battle1": Stage(graphics.get("battle1")),
        "battle2": Stage(graphics.get("battle2"))
        
    }
    
    return stages.get(stage_name)