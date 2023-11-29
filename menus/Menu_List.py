"""
Contains all of the menus for the game.
"""
from menus.Menu import Menu

def get_menu(menu_name:str):
    menu_list = {
        "START MENU": Menu("CMD Adventure", ["Create Character", "Quit"]),
        "CHARACTER CREATION": Menu("Create Character", [""]),
        "START GAME": Menu("CMD Adventure", ["Start game", "Quit"]),
        "CLASS MENU": Menu("Select Class", ["Rouge", "Warrior"])
    }
    
    return menu_list.get(menu_name)