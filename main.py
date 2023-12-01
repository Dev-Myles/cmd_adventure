"""
Contains the main logic for our program
"""

from state.State import State
from state.state_processes import * 
from system.System import System

def main():
    while True: 
        System.clear_screen()
        STATE = State("START MENU","START MENU", False)
        while True:
            if STATE.is_stage() == "START MENU":
                character_creation_process(STATE)          
            elif STATE.is_stage() == "PLAY GAME":
                play_game(STATE)
                combat(STATE)
            elif STATE.is_stage() == "END":
                selection = replay(STATE)
                if selection == "RESTART":
                    break
                elif selection == "RETRY FIGHT":
                    STATE.set_stage("PLAY GAME")
    

if __name__ == "__main__":
    main()
