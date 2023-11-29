"""
This file contains all of the logic for the menus that are displayed
"""
import sys

from validation.Input_Validation import Input_Validation

class Menu(Input_Validation):
    def __init__(self, name:str, options:list) -> None:
        self.name = name
        self.options = options
    
    def change_menu(self, options:list) -> None:
        self.options = options
    
    def show_menu(self) -> None:
        list_string = ""
        print(f"\n{self.name}\n")
        for ops in self.options:
            list_string += f"| {ops}\t"
        return print(list_string)
    
    def select_option(self) -> None:
        user_selection = self.val_input_from_list(self.options, "str")
        
        if user_selection.lower() == "quit":
            return  sys.exit()
        else:
            return user_selection
    
    
