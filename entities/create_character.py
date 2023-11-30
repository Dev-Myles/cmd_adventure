"""
This file contains the logic for creating a player character.
"""
from menus import Menu_List
from system.System import System


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
    System.clear_screen()
    CLASS_MENU = Menu_List.get_menu("CLASS MENU")
    print("\n")
    bar = "-"*75
    enter_name_message ="Enter the name of your character".center(71)
    
    print(bar)
    print(f"| {enter_name_message} |")
    print(bar)
    
    character_name = input("")
    
    System.clear_screen()
    
    CLASS_MENU.show_menu()
    
    selected_class = CLASS_MENU.select_option()
    
    input("\nCharacter has been created.\nPress enter to continue...\n")
        
    class_stats = get_player_class(selected_class.strip())
    
    return {"name": character_name,
            "health": class_stats.get("health"),
            "damage": class_stats.get("damage"),
            "selected_class": selected_class
    }
    