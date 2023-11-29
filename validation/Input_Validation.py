"""
This file contains the logic for testing user input from std input.
"""

class Input_Validation:
    def __init__(self) -> None:
        pass
    
    def val_input_type(self, user_input: str, exp_type: str) -> list:
        match exp_type:
            case "int":
                try:
                    int(user_input)
                    return [True, int(user_input)]
                except ValueError:
                    return [False, ""]  
            case "float":
                try:
                    float(user_input)
                    return [True, float(user_input)]
                except ValueError:
                    return [False, ""]
            case "str":
                try:
                    str(user_input)
                    return [True, str(user_input)]
                except ValueError:
                    return [False, ""]

            case _: 
                return [False, ""]
    
    def user_val_loop(
    self,
    message: str,
    error_message: str,
    exp_type: str
    ) -> int | str | float:
        func_val = [False, ""]
    
        while not func_val[0]: 
            user_input = input(f"{message}: ")
            func_val = self.val_input_type(user_input, exp_type) 
            if func_val[0]:
                return func_val[1]
            elif not func_val[0]:
                print(error_message)
                continue
        
    def val_input_from_list(self, ops_list: list, exp_type:str) -> None:
        while True:
            user_input = self.user_val_loop(
                "Please enter an option from the list",
                "That is not a valid input, try again.\n",
                exp_type
            )
            
            sanitized_ops_list = map(lambda x:x.lower(), ops_list)

            if user_input in sanitized_ops_list:
                return user_input
            else:
                print(user_input)
                print("That is not option, please try again.")
                input("\nPress enter to continue...\n")
                continue
