## This is a the main application file for FreezeDB.
## It will be slowly updated as I understand more
## and more.

# SET NAME
app = __name__ # used in run.py

# IMPORT EXTERNAL
from sqlalchemy import create_engine, text, MetaData, insert
from sqlalchemy.orm import sessionmaker, relationship, declarative_base, registry, Session

# IMPORT INTERNAL
from freezedb.database_classes import Sample, Location, Base, mapper_registry

# SETTINGS
engine = create_engine("sqlite:///freeze.db", echo=True, future=True) # Configure SQL database using engine object (echo = logging)
session = Session(engine)

# WRITE TO DB
mapper_registry.metadata.create_all(engine)
Base.metadata.create_all(engine)

# DISPLAY SWITCH STATEMENTS

# PRINT OUT CURRENT DB DATA
u1 = Sample(participant_id = 4001)
print(u1.blood_type)
session.query(Sample)
test = session.query(Sample)
# REFPECTION

# TEST WRITTING CLASSES
""" testData = Sample(participant_id = 4002, identifier = 1, blood_type = "plasma", date = "Dadadad")
session.add(testData)
print(f"session is: {session.new}")
session.flush() # push
session.commit() # commit
 """
# PROGRAM FINISHED
print("Program finished!")
print(test)
print(sess)
