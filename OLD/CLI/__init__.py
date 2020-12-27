# This is a the main application file for FreezeDB.
# It will be slowly updated as I understand more
# and more.

# IMPORT
# External modules
from sqlalchemy import create_engine, text, MetaData, insert
from datetime import datetime

# Internal modules
from classes import Blood, Urine, Sample, Base
from functions import delete, lookup, settings, quit, engine, session
from modules.insert import data_input
from modules.export import export
from modules.menu import menu

# SET NAME
app = __name__

# SETTINGS
Base.metadata.create_all(engine)

# SHOW FIRST MENU
selection = menu(level="main", sub_menu="NA", setting="default")

# Menu loop
while selection.level.upper() != "Q":
    # Go to submenu
    selection = menu(level=selection.level, setting=selection.setting)

    # Main menu (return)
    if selection.level.upper() == "R":
        selection = menu(level="main", sub_menu="NA", setting="default")
    
    ## SUBMENUS FUNCTIONS
    # Data input
    elif selection.level == "1":
        selection = data_input(sub_menu=selection.sub_menu, setting=selection.setting)

    # Delete
    elif selection.level == "2":
        delete(selection.sub_menu)

    # Lookup/query
    elif selection.level == "3":
        selection = lookup(selection.sub_menu)

    # Export
    elif selection.level == "4":
        selection = export(sub_menu=selection.sub_menu)

    # Settings
    elif selection.level == "5":
        settings(selection.sub_menu)

    # Invalid input
    else:
        print("Invalid input. Try again")
        selection = menu()
    

# QUIT
quit()









# Testing stuff
# QUERY DATABASe
query_test = session.query(Blood).filter_by(participant_id=4005).first()

# WRITE DATA
u1 = Blood(participant_id=4005, identifier=2, blood_type="Plasma")
print(u1.blood_type)
session.query(Sample)
test = session.query(Sample)
print(test)

# TEST WRITTING CLASSES
testData = Blood(
    participant_id=4003,
    identifier=1,
    blood_type="plasma",
    visit="Baseline",
    date_time=datetime.now(),
)

session.add(testData)
print(f"session is: {session.new}")
session.flush()  # push
session.commit()  # commit

# PROGRAM FINISHED
print("Program finished!")
print(test)
