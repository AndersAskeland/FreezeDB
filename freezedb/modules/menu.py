# The menu module. This module is responbile for showing
# and doing menu stuff. I might turn the menu into classes.


## IMPORT STUFF ##
# External
import os

# internal
from freezedb.classes import ReturnValue


## MENU PRINT
# Main menu
def main_menu():
    # Clear terminal
    os.system('cls' if os.name == 'nt' else 'clear') # clear terminal - multi-platform
    
    # Menu print
    print("###################################")
    print("############ FreezeDB #############")
    print("###################################")
    print("What do you want to do?")
    print("   [1] Input database values.")
    print("   [2] Delete database values.")
    print("   [3] View data.")
    print("   [4] Settings")
    print("   [Q] Quit program")


def sub_menu_input(val = 0):
    # Clear terminal
    os.system('cls' if os.name == 'nt' else 'clear') # clear terminal - multi-platform

    print("Choose database")
    print("  [1] Blood sample DB")
    print("  [2] Urine sample DB")
    if val == 1:
        print("  [3] Write to DB")
    print("  [R] Return")
    print("  [Q] Quit program")



def sub_menu_delete(test):
    print("Choose database")
    print("  [1] Blood sample DB")
    if test == "1":
        print("woho")
    print("  [2] Urine sample DB")
    print("  [3] Return")

    input("Fasdfas")
def sub_menu_lookup():
    print("Choose database")
    print("  [1] Blood sample DB")
    print("  [2] Urine sample DB")
    print("  [3] Return")

def sub_menu_settings():
    print("Choose database")
    print("  [1] Blood sample DB")
    print("  [2] Urine sample DB")
    print("  [3] Return")




## MENU FUNCTION
# Menu
def menu(main_lvl=0, setting=0):
    # This function defines the menu which is to be presented to the user
    # it can either be a standard menu, or an altered menu, based on settings = 1.
    # Standard menus
    if setting == 0:
        # Main menu
        if main_lvl == 0:
            main_menu()
            selection = int(input("Selection: ")) # arg0
            return ReturnValue(selection, main_lvl, None)

        # Input
        elif main_lvl == 1:
            sub_menu_input()
            selection = int(input("Selection: ")) # arg0
            return ReturnValue(selection, main_lvl, None)

        # delete
        elif main_lvl == 2:
            sub_menu_delete()
            selection = int(input("Selection: ")) # arg0
            return ReturnValue(selection, main_lvl, None)

        # lookup
        elif main_lvl == 3:
            sub_menu_lookup()
            selection = int(input("Selection: ")) # arg0
            return ReturnValue(selection, main_lvl, None)

        # settings
        elif main_lvl == 4:
            sub_menu_settings()
            selection = int(input("Selection: ")) # arg0
            return ReturnValue(selection, main_lvl, None) 
    
    # Conditional menu
    if setting == 1:
        # Main menu
        if main_lvl == 0:
            main_menu()
            selection = int(input("Selection: ")) # arg0
            return ReturnValue(selection, main_lvl, None)

        # Input
        elif main_lvl == 1:
            sub_menu_input(1)
            selection = int(input("Selection: ")) # arg0
            return ReturnValue(selection, main_lvl, None)

        # delete
        elif main_lvl == 2:
            sub_menu_delete()
            selection = int(input("Selection: ")) # arg0
            return ReturnValue(selection, main_lvl, None)

        # lookup
        elif main_lvl == 3:
            sub_menu_lookup()
            selection = int(input("Selection: ")) # arg0
            return ReturnValue(selection, main_lvl, None)

        # settings
        elif main_lvl == 4:
            sub_menu_settings()
            selection = int(input("Selection: ")) # arg0
            return ReturnValue(selection, main_lvl, None)          

