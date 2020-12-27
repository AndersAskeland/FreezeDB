# The menu module. This module is responbile for showing
# and doing menu stuff. I might turn the menu into classes.


## IMPORT STUFF ##
# External
from operator import le
import os

# internal
from classes import MenuSelection


## MENU PRINT - What gets printet to the screen
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
    print("   [4] Export data.")
    print("   [5] Settings")
    print("   [Q] Quit program")


# Input database value
def sub_menu_input(val = 0):
    # Clear terminal
    os.system('cls' if os.name == 'nt' else 'clear') # clear terminal - multi-platform

    # Menu print
    print("Choose database")
    print("  [1] Blood sample DB")
    print("  [2] Urine sample DB")
    if val == 1:
        print("  [3] Write to DB")
    print("  [R] Return")
    print("  [Q] Quit program")


# Delete database stuff
def sub_menu_delete(test):
    print("Choose database")
    print("  [1] Blood sample DB")
    if test == "1":
        print("woho")
    print("  [2] Urine sample DB")
    print("  [3] Return")

    input("Fasdfas")

# Lookup data
def sub_menu_lookup():
    print("Which database do you want to write from?")
    print("  [1] Blood sample DB")
    print("  [2] Urine sample DB")
    print("  [3] Return")

# Export data
def sub_menu_export():
    # Clear terminal
    os.system('cls' if os.name == 'nt' else 'clear') # clear terminal - multi-platform

    # Menu print
    print("Which database do you want to write from?")
    print("  [1] Blood sample DB")
    print("  [2] Urine sample DB")
    print("  [R] Return")
    print("  [Q] Quit program")


# Settings menu
def sub_menu_settings():
    print("Choose database")
    print("  [1] Blood sample DB")
    print("  [2] Urine sample DB")
    print("  [3] Return")


def sub_sub_menu_export():
    print("Choose database")
    print("  [1] All data")
    print("  [2] Select data")
    print("  [R] Return")



## MENU FUNCTION
# Menu
def menu(level="main", sub_menu="NA", setting="default"):
    # This function defines the menu which is to be presented to the user
    # it can either be a standard menu, or an altered menu, based on settings = 1.
    
    
    # Default settings
    if setting == "default":
        
        # Main menu
        if level == "main":
            # Show menu
            main_menu()            
            
            # Return selection
            return MenuSelection(level=str(input("Selection: ")), sub_menu="NA", setting=setting)

        # Input
        elif level == "1":
            # Show menu
            sub_menu_input()

            # Return seleciton
            return MenuSelection(level=level, sub_menu=str(input("Selection: ")), setting=setting)

        # delete
        elif level == "2":
            sub_menu_delete()
            return MenuSelection(level=level, sub_menu=str(input("Selection: ")), setting=setting)

        # lookup
        elif level == "3":
            sub_menu_lookup()
            return MenuSelection(level=level, sub_menu=str(input("Selection: ")), setting=setting)
        
        # Export
        elif level == "4":
            sub_menu_export()
            return MenuSelection(level=level, sub_menu=str(input("Selection: ")), setting=setting)
        
        # settings
        elif level == "5":
            sub_menu_settings()
            return MenuSelection(level=level, sub_menu=str(input("Selection: ")), setting=setting)
    
    # Conditional menu - Alternative state for menu
    if setting == "alternative":
        # Main menu
        if level == "0":
            main_menu()
            return MenuSelection(level=level, sub_menu=str(input("Selection: ")), setting=setting)

        # Input
        elif level == "1":
            sub_menu_input(1)
            return MenuSelection(level=level, sub_menu=str(input("Selection: ")), setting=setting)

        # delete
        elif level == "2":
            sub_menu_delete()
            return MenuSelection(level=level, sub_menu=str(input("Selection: ")), setting=setting)

        # lookup
        elif level == "3":
            sub_menu_lookup()
            return MenuSelection(level=level, sub_menu=str(input("Selection: ")), setting=setting)
        
        # Export 
        elif level == "4":
            sub_menu_export()
            return MenuSelection(level=level, sub_menu=str(input("Selection: ")), setting=setting)
        
        # settings
        elif level == "5":
            sub_menu_settings()
            return MenuSelection(level=level, sub_menu=str(input("Selection: ")), setting=setting)

    # Invalid input/return with default (R & Q)
    return MenuSelection(level=level, sub_menu=None, setting=None)

