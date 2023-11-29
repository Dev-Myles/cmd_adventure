"""
This file contains the logic for creating a player character.
"""
from menus import Menu_List
from .Entity import Entity


def get_player_class(class_type:str) -> dict:
    classes = { 
                "warrior": {
                    "health": 40,
                    "damage": 8
                },
                "rouge": {
                    "health": 32,
                    "damage": 14
                },
            }
    
    return classes.get(class_type)

def create_character():
    CLASS_MENU = Menu_List.get_menu("CLASS MENU")
    
    character_name = input("Enter the name of your character: ")
    
    CLASS_MENU.show_menu()
    
    selected_class = CLASS_MENU.select_option()
    
    class_stats = get_player_class(selected_class)
    
    return Entity(character_name,
                class_stats.get("health"),
                class_stats.get("damage")
                )
    