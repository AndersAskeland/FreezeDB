# A file containing all the different functions that are possible.
import sys, os


# MENU
def menu():
    print("What do you want to do?")
    print("   [1] Input database values.")
    print("   [2] Delete database values.")
    print("   [3] View data.")
    print("   [4] Settings")
    print("   [5] Quit program\n")

def menu_data_input():
    print("Choose database")
    print("  [1] Blood sample DB")
    print("  [2] Urine sample DB")
    print("  [3] Return")


# WELCOME
def welcome():
    print("###################################")
    print("####### Welcome to FreezeDB #######")
    print("###################################\n")


def blood_db():
    print("Blooood")


def urine_db():
    print("Urine")


# INPUT
def data_input():
    print("## Input Data ##")
    menu_data_input()


    # Take input
    selection_func = int(input("Selection: "))
    
    # Enter function
    while selection_func != 3:
        if selection_func == 1:
            blood_db()
        elif selection_func == 2:
            urine_db()
        
        # New input
        os.system('cls' if os.name == 'nt' else 'clear')    
        print("## Input Data ##")
        menu_data_input()        
        selection_func = int(input("Selection: "))



# DELETE
def delete():
    print("Delete menu")


# VIEW
def lookup():
    print("View menu")


# SETTINGS
def settings():
    print("Settings menu")


# EXIT
def quit():
    sys.exit("Exiting program")

