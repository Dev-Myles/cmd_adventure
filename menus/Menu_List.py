"""
Contains all of the menus for the game.
"""
from menus.Menu import Menu
from stages.Stage import Stage
from graphics.graphics import graphics

def get_menu(menu_name:str):
    menu_list = {
        "START MENU": Menu("CMD Adventure", ["Create Character", "Quit"]),
        "CHARACTER CREATION": Menu("Create Character", [""]),
        "START GAME": Menu("CMD Adventure", ["Play Game", "Quit"]),
        "CLASS MENU": Menu("Select Class", ["Rouge", "Warrior"]),
        "PLAY GAME": Menu("","", graphics.get("road")),
        "END": Menu("End Screen",["Restart","Retry Fight", "Quit"])
    }
    
    return menu_list.get(menu_name)