"""
Contains the main logic for our program
"""

from state.State import State
from menus.Menu import Menu
from menus.Menu_List import get_menu
from entities.create_character import create_character



def main():
    STATE = State("START MENU","START MENU", False)

    while True:
        CURRENT_MENU = get_menu(STATE.is_stage())
        CURRENT_MENU.show_menu()
        user_selection = CURRENT_MENU.select_option()
        STATE.set_stage(user_selection.upper())
        if STATE.current_stage == 'CREATE CHARACTER':
            created_character = create_character()
            STATE.player_info = created_character
            STATE.set_stage("START GAME")
            continue
    
    

if __name__ == "__main__":
    main()
