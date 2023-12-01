"""
This file contains the functions that will help transition to the correct graphics and state.
"""
from state.State import State
from menus.Menu import Menu
from menus.Menu_List import get_menu
from entities.create_character import create_character
from entities.Entity import Entity
from stages.stages import stage_list
from system.System import System
import random

import time

def character_creation_process(STATE):
    GAME_TITLE = stage_list("title")
    while STATE.current_stage != "PLAY GAME":
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
            System.clear_screen()
            continue
    return 

def play_game(STATE):
    player_class = STATE.player_info.get("selected_class")
    System.clear_screen()
    print("\nYou set off on your journey to slay the dragon that has taken over the CMD castle.")
    stage_list(player_class).display_stage()
    stage_list("road1").display_stage()
    time.sleep(5.0)
    print(f"\t\t\tThe journey is long and arduous, but you are a master {player_class}.\n\t\t\tYou see the towers of the towers off in the distance.\n")
    stage_list("road2").display_stage()
    time.sleep(5.0)
    print("The front of the castle is charred.")
    time.sleep(1.0)
    print("Shattered bodies and wagons are scattered in its court yard.")
    time.sleep(1.0)
    print("You enter the castle...")
    time.sleep(5.0)
    System.clear_screen()
    print("…And you come face to face with the wretched dragon!")
    if player_class == "rouge":
        stage_list("battle_rouge").display_stage()
    else:
        stage_list("battle_warrior").display_stage()
    
    time.sleep(1.0)
    print("Is bright red scales match the blood on the wall...")
    time.sleep(1.0)
    print("He looks your way...")
    time.sleep(1.0)
    print("...And attacks!")
    time.sleep(3.0)
    STATE.set_stage("COMBAT")
    return

def combat(STATE):
    System.clear_screen()
    stage_list("fight").display_stage()
    dragon = Entity("Dragon", 50, 15, "monster", 12)
    player = Entity(STATE.player_info.get("name"), 
                    STATE.player_info.get("health"),
                    STATE.player_info.get("damage"),
                    STATE.player_info.get("selected_class"),
                    10
                    )
    
    while dragon.health > 0 and player.health > 0:
        player_attack =  player.attack()
        dragon.set_health(player_attack)
        dragon.show_health()
        time.sleep(1.5)
        if dragon.health > 0:
            dragon_attack = dragon.attack()
            player.set_health(dragon_attack)
            player.show_health()
            time.sleep(1.5)
        else:
            break
        continue
    
    if dragon.health <= 0:
        System.clear_screen()
        stage_list("player_win").display_stage()
        STATE.set_stage("END")
    elif player.health <= 0:
        System.clear_screen()
        stage_list("dragon_win").display_stage()
        STATE.set_stage("END")
        
    return


def replay(STATE):
    time.sleep(3)
    System.clear_screen()
    player_name = STATE.player_info.get("name")
    print(f"Would you like to play again {player_name}")
    CURRENT_MENU = get_menu(STATE.is_stage())
    CURRENT_MENU.show_menu() 
    user_selection = CURRENT_MENU.select_option()
    return user_selection.upper()
    