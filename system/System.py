"""
This file contains the System class which contains
logic for general system functionality.
"""

import os

class System:
    def __init__(self) -> None:
        pass
    
    def clear_screen():
        # For Windows
        if os.name == 'nt':
            _ = os.system('cls')
    
        # For macOS and Linux
        else:
            _ = os.system('clear')