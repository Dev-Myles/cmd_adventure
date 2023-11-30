"""
This file contains all of the logic for the menus that are displayed
"""
import sys

from validation.Input_Validation import Input_Validation

class Menu(Input_Validation):
    
    def __init__(self, name:str, options:list, graphic: str = "") -> None:
        self.name = name
        self.options = options
        self.graphic = graphic
    
    def select_option(self) -> None:
        user_selection = self.val_input_from_list(self.options, "str")
        
        if user_selection.lower() == "quit":
            return  sys.exit()
        else:
            return user_selection
    
    def show_menu(self) -> None:
        if self.graphic == "":
            bar = "-"*75
            print(bar)
            for option in self.options:
                header = str(option).center(71)
                print(f"| {header} |")

            print(bar)
        else:
            print(self.graphic)
    
