# This is a the main application file for FreezeDB.
# It will be slowly updated as I understand more
# and more.

# IMPORT
# External modules
from sqlalchemy import create_engine, text, MetaData, insert
from sqlalchemy.orm import (
    sessionmaker,
    relationship,
    declarative_base,
    registry,
    Session
)
from datetime import datetime

# Internal modules
from freezedb.database_classes import Blood, Urine, Sample, Location, Base

# SET NAME
app = __name__

# SETTINGS
engine = create_engine("sqlite:///freeze.db", echo=True, future=True)  # Configure SQL database using engine object (echo = logging)
session = Session(bind=engine)

# WRITE TO DB
Base.metadata.create_all(engine)
session.add_all()

# DISPLAY SWITCH STATEMENTS

# QUERY DATABASe
query_test = session.query(Blood).filter_by(participant_id=4005).first()

# WRITE DATA
u1 = Sample(participant_id=4005, identifier=2, blood_type="Plasma")
print(u1.blood_type)
session.query(Sample)
test = session.query(Sample)
print(test)

# TEST WRITTING CLASSES
testData = Sample(
    participant_id=4003,
    identifier=1,
    blood_type="plasma",
    visit="Baseline",
    date=datetime.now(),
)
session.add(testData)
print(f"session is: {session.new}")
session.flush()  # push
session.commit()  # commit

# PROGRAM FINISHED
print("Program finished!")
print(test)
