# The export module. This module is responbile for exporting data to CSV files
# At some point maybe also to other stuff.

## IMPORT MODULES
# External


# Internal
from classes import MenuSelection, Blood, Urine
from functions import read_sql, write_csv

## SETTINGS


# MAIN
def export(sub_menu):
    # Blood database
    if sub_menu == "1":
        # Menu
        print("Write sample id. Press enter to export all data")

        # Inputs required
        database = str(input("Selection: "))

        # Write all to CSV
        if database == "":
            sql_data = read_sql(db=Blood)
            write_csv(sql_data)

        # Write selection to csv
        else:
            sql_data = read_sql(db=Blood, participant_id=database)

            write_csv(sql_data)

        # Return
        return MenuSelection(level="4", sub_menu=sub_menu, setting="default")
    
    # Urine database
    elif sub_menu == "2":
        pass
    
    # Return to main menu or exit
    elif sub_menu.upper() == "R" or sub_menu.upper() == "Q":
        return MenuSelection(level=sub_menu, sub_menu=None, setting=None)


    # Error checking
    else:
        print("Invalid input. Try again.")
        return MenuSelection(level="4", sub_menu=sub_menu, setting="default")



