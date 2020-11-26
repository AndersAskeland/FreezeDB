# This is a the main application file for FreezeDB.
# It will be slowly updated as I understand more
# and more.

# IMPORT
# External modules
from sqlalchemy import create_engine, text, MetaData, insert
import os
from datetime import datetime
from sqlalchemy.orm import (
    sessionmaker,
    relationship,
    declarative_base,
    registry,
    Session
    )

# Internal modules
from freezedb.database_classes import Blood, Urine, Sample, Base
from freezedb.modules import data_input, delete, lookup, settings, quit, menu, welcome

# SET NAME
app = __name__

# SETTINGS
engine = create_engine("sqlite:///freeze.db", echo=True, future=True)  # Configure SQL database using engine object (echo = logging)
session = Session(bind=engine)

# SWITCH MENU


# WRITE TO DB
Base.metadata.create_all(engine)


# DISPLAY MAIN SWITCH(IF/ELIF CHAIN) STATEMENTS #
# Print menu
welcome()
menu()

# gather input
selection = int(input("Selection: "))
os.system('cls' if os.name == 'nt' else 'clear') # clear terminal - multi-platform

while selection != 5:
    if selection == 1:
        data_input()
    elif selection == 2:
        delete()
    elif selection == 3:
        lookup()
    elif selection == 4:
        settings()
    
    # New input
    menu()
    selection = int(input("Selection: "))

# Exit program
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
