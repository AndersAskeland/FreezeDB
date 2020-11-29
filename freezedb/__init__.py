# This is a the main application file for FreezeDB.
# It will be slowly updated as I understand more
# and more.

# IMPORT
# External modules
from sqlalchemy import create_engine, text, MetaData, insert
from datetime import datetime

# Internal modules
from freezedb.classes import Blood, Urine, Sample, Base
from freezedb.modules.etc import delete, lookup, settings, quit, engine, session
from freezedb.modules.insert import data_input
from freezedb.modules.menu import menu

# SET NAME
app = __name__

# SETTINGS
Base.metadata.create_all(engine)

# SHOW MENU
selection = menu()

print(selection.arg0.upper())
# Menu loop
while selection.arg0.upper() != "Q":
    selection = menu(main_lvl=selection.arg0, setting=selection.arg1)

    # return
    if selection.arg0.upper() == "R":
        selection = menu()
    
    # Data input
    elif selection.arg1 == "1":
        selection = data_input(selection.arg0)

    # Delete
    elif selection.arg1 == "2":
        delete(selection.arg0)

    # Lookup/query
    elif selection.arg1 == "3":
        lookup(selection.arg0)

    # Settings
    elif selection.arg1 == "4":
        settings(selection.arg0)

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
