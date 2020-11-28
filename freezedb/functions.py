# A file containing all the different functions that are possible.

# IMPORT
# External modules
import sys, os
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


# Internal modules
from freezedb.classes import Blood, Urine, Sample, ReturnValue
from freezedb.menu import main_menu, sub_menu_input, sub_menu_delete, sub_menu_lookup, sub_menu_settings


# SETTINGS
engine = create_engine("sqlite:///freeze.db", echo=True, future=True)  # Configure SQL database using engine object (echo = logging)
session = Session(bind=engine)

# MENU
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


# INPUT
def data_input(selection):
    # Blood database
    if selection == 1:
        # Inputs required
        participant_id = int(input("Participant ID: "))
        visit = str(input("Visit: "))
        blood_type = str(input("Blood type: "))

        # Add to class
        dat = Blood(participant_id=participant_id, visit=visit, blood_type=blood_type)

        # Add to session
        session.add(dat)

        # Return
        return ReturnValue(1, 1, None)
    
    # Urine database
    elif selection == 2:
        # Inputs required
        participant_id = int(input("Participant ID: "))
        visit = str(input("Visit: "))
        
        # Add to class
        dat = Urine(participant_id=participant_id, visit=visit)

        # Add to session
        session.add(dat)

        # Return
        return ReturnValue(1, 1, None)
    
    # Comit to db
    elif selection == 3:
        session.flush()
        session.commit()
        return ReturnValue(1, 0, None)
    
    else:
        pass


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

