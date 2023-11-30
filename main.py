"""
Contains the main logic for our program
"""

from state.State import State
from menus.Menu import Menu
from menus.Menu_List import get_menu
from entities.create_character import create_character
from stages.stages import stage_list



def main():
    STATE = State("START MENU","START MENU", False)
    GAME_TITLE = stage_list("title")
    print("TOPE OF asdfasfasdfasdfasfd")

        
    while True:
            if STATE.current_stage == 'PLAY GAME':
                print("playing game")
            GAME_TITLE.display_stage()
            STATE.display_player_name()
            CURRENT_MENU = get_menu(STATE.is_stage())
            CURRENT_MENU.show_menu() 
            user_selection = CURRENT_MENU.select_option()
            STATE.set_stage(user_selection.upper())
            
            if STATE.current_stage == 'CREATE CHARACTER' and not STATE.created_player and not STATE.is_playing:
                created_character = create_character()
                STATE.player_info = created_character
                STATE.set_stage("START GAME")
                print('HERER')
                continue
     
        
        
        # while True:
        #     CURRENT_MENU = get_menu(STATE.is_stage())
        #     CURRENT_MENU.show_menu() 
        #     user_selection = CURRENT_MENU.select_option()
        #     STATE.set_stage(user_selection.upper())
        #     break
        
        # while True:
        #     print("playing game")
        #     break
        
        # print("main loop")
    
    

if __name__ == "__main__":
    main()
