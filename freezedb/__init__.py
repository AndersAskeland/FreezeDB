# This is a the main application file for FreezeDB.
# It will be slowly updated as I understand more
# and more.

# IMPORT
# External modules
from sqlalchemy import create_engine, text, MetaData, insert
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
from freezedb.modules import data_input, delete, lookup, settings, quit

# SET NAME
app = __name__

# SETTINGS
engine = create_engine("sqlite:///freeze.db", echo=True, future=True)  # Configure SQL database using engine object (echo = logging)
session = Session(bind=engine)

# SWITCH MENU


# WRITE TO DB
Base.metadata.create_all(engine)

# DISPLAY MAIN SWITCH(IF/ELIF CHAIN) STATEMENTS #
# show options
print("###################################")
print("####### Welcome to FreezeDB #######")
print("###################################\n")
print("What do you want to do?")
print("   1. Input database values.")
print("   2. Delete database values.")
print("   3. View data.")
print("   4. Settings")
print("   5. Quit program\n")

# gather input
switch = int(input("Enter: "))

# error check input
# USE FUNCTION
if switch == 1:
    data_input()
elif switch == 2:
    delete()
elif switch == 3:
    lookup()
elif switch == 4:
    settings()
elif switch == 5:
    quit()

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
