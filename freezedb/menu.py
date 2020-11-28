# A file containing all the different functions that are possible. I might possibly in the future
# turn these into classes. 

# Modules
import os

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
    print("   [Q] Quit program\n")


def sub_menu_input(val = 0):
    print("Choose database")
    print("  [1] Blood sample DB")
    print("  [2] Urine sample DB")
    if val == 1:
        print("  [3] Write to DB")
    print("  [R] Return")
    print("  [Q] Quit program\n")



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


